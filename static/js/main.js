document.addEventListener('DOMContentLoaded', () => {

    // --- CART LOGIC ---
    const cartOverlay = document.querySelector('.cart-overlay');
    const cartSidebar = document.querySelector('.cart-sidebar');
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const fullPageCartList = document.getElementById('full-cart-items-list');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const openCart = () => {
        if (cartOverlay && cartSidebar) {
            cartOverlay.classList.add('is-open');
            cartSidebar.classList.add('is-open');
        }
    };
    const closeCart = () => {
        if (cartOverlay && cartSidebar) {
            cartOverlay.classList.remove('is-open');
            cartSidebar.classList.remove('is-open');
        }
    };
    const saveCart = () => {
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartUI();
    };
    const addToCart = (item) => {
        const existingItem = cart.find(cartItem => cartItem.id === item.id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ ...item, quantity: 1 });
        }
        saveCart();
    };
    const updateQuantity = (id, change) => {
        const item = cart.find(cartItem => cartItem.id === id);
        if (item) {
            item.quantity += change;
            if (item.quantity <= 0) {
                removeItem(id);
            } else {
                saveCart();
            }
        }
    };
    const removeItem = (id) => {
        cart = cart.filter(item => item.id !== id);
        saveCart();
    };
    const updateCartUI = () => {
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        
        const cartIconLink = document.getElementById('cart-icon-link');
        if (cartIconLink) {
            const existingCount = cartIconLink.querySelector('.cart-item-count');
            if (existingCount) existingCount.remove();
            if (totalItems > 0) {
                const countSpan = document.createElement('span');
                countSpan.className = 'cart-item-count';
                countSpan.textContent = totalItems;
                cartIconLink.appendChild(countSpan);
            }
        }
        
        if (cartSidebar) {
            cartSidebar.innerHTML = `
                <div class="cart-header"><h3>Cart</h3><button class="cart-close-btn">×</button></div>
                <div class="cart-body">
                    ${cart.length > 0 ? cart.map(item => `
                        <div class="cart-item">
                            <img src="${item.image}" alt="${item.name}">
                            <div class="item-details">
                                <p class="item-name">${item.name}</p>
                                <p class="item-price">$${item.price.toFixed(2)}</p>
                                <div class="quantity-control">
                                    <button class="quantity-btn" data-id="${item.id}" data-change="-1">-</button>
                                    <span>${item.quantity}</span>
                                    <button class="quantity-btn" data-id="${item.id}" data-change="1">+</button>
                                </div>
                            </div>
                            <div class="item-total">$${(item.price * item.quantity).toFixed(2)}</div>
                            <button class="cart-item-remove-btn" data-id="${item.id}"><i class="fa-solid fa-trash-can"></i></button>
                        </div>`).join('') : '<p class="cart-empty-msg">Your cart is empty.</p>'}
                </div>
                <div class="cart-footer">
                    <div class="subtotal-row"><span>Subtotal</span><span>$${subtotal.toFixed(2)}</span></div>
                    <a href="/cart/" class="view-cart-btn-sidebar">View Cart</a>
                </div>`;
        }

        if (fullPageCartList) {
            fullPageCartList.innerHTML = `${cart.length > 0 ? cart.map(item => `
                <div class="full-cart-item">
                    <img src="${item.image}" alt="${item.name}">
                    <div class="item-info"><p class="item-name">${item.name}</p><p class="item-price">$${item.price.toFixed(2)}</p></div>
                    <div class="quantity-control">
                        <button class="quantity-btn" data-id="${item.id}" data-change="-1">-</button>
                        <span>${item.quantity}</span>
                        <button class="quantity-btn" data-id="${item.id}" data-change="1">+</button>
                    </div>
                    <div class="item-total-full">$${(item.price * item.quantity).toFixed(2)}</div>
                    <button class="cart-item-remove-btn" data-id="${item.id}"><i class="fa-solid fa-trash-can"></i></button>
                </div>`).join('') : '<p class="cart-empty-msg">Your cart is empty. <a href="/order-online/">Continue shopping</a>.</p>'}`;
            const summarySubtotal = document.getElementById('summary-subtotal');
            const summaryTotal = document.getElementById('summary-total');
            if (summarySubtotal && summaryTotal) {
                summarySubtotal.textContent = `$${subtotal.toFixed(2)}`;
                summaryTotal.textContent = `$${subtotal.toFixed(2)}`;
            }
        }
    };

    document.body.addEventListener('click', (e) => {
        const cartIcon = e.target.closest('#cart-icon-link');
        if (cartIcon) {
            e.preventDefault();
            openCart();
        }
        if (e.target.classList.contains('cart-close-btn') || e.target.classList.contains('cart-overlay')) closeCart();
        if (e.target.matches('.quantity-btn')) updateQuantity(e.target.dataset.id, parseInt(e.target.dataset.change, 10));
        if (e.target.closest('.cart-item-remove-btn')) removeItem(e.target.closest('.cart-item-remove-btn').dataset.id);
    });
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const { id, name, price, image } = e.target.dataset;
            addToCart({ id, name: name, price: parseFloat(price), image: image });
            openCart();
        });
    });
    
    const promoLink = document.getElementById('promo-link');
    if (promoLink) promoLink.addEventListener('click', (e) => { e.preventDefault(); document.getElementById('promo-input-container').classList.toggle('hidden'); });
    const noteLink = document.getElementById('note-link');
    if (noteLink) noteLink.addEventListener('click', (e) => { e.preventDefault(); document.getElementById('note-input-container').classList.toggle('hidden'); });
    
    updateCartUI();
    
    // --- HOMEPAGE SLIDER ---
    const heroSlides = document.querySelectorAll('.hero-slide');
    if (heroSlides.length > 0) {
        let currentSlideIndex = 0;
        heroSlides[0].classList.add('active');

        const showNextSlide = () => {
            const previousSlideIndex = currentSlideIndex;
            currentSlideIndex = (currentSlideIndex + 1) % heroSlides.length;
            
            heroSlides[previousSlideIndex].classList.add('previous');
            heroSlides[previousSlideIndex].classList.remove('active');
            heroSlides[currentSlideIndex].classList.add('active');
            
            setTimeout(() => {
                heroSlides[previousSlideIndex].classList.remove('previous');
            }, 1000);
        };
        setInterval(showNextSlide, 3000);
    }

    // --- GALLERY SCROLLER ---
    const gallerySection = document.querySelector('.gallery-section');
    if (gallerySection) {
        const numOriginalItems = 5;
        const itemWidth = 180 + 10;
        let galleryIndex = 0;
        gallerySection.style.transition = 'transform 0.5s ease-in-out';

        const scrollGallery = () => {
            galleryIndex++;
            gallerySection.style.transform = `translateX(-${galleryIndex * itemWidth}px)`;
            
            if (galleryIndex === numOriginalItems) {
                setTimeout(() => {
                    gallerySection.style.transition = 'none';
                    galleryIndex = 0;
                    gallerySection.style.transform = 'translateX(0)';
                    void gallerySection.offsetWidth;
                    gallerySection.style.transition = 'transform 0.5s ease-in-out';
                }, 500);
            }
        };
        setInterval(scrollGallery, 2500);
    }

    // --- BOOKING FLOW LOGIC ---

    // 1. Save selected workshop details when "Book Now" is clicked
    const bookNowLinks = document.querySelectorAll('.book-now-link');
    bookNowLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const workshopData = {
                name: e.currentTarget.dataset.name,
                duration: e.currentTarget.dataset.duration,
                price: e.currentTarget.dataset.price
            };
            localStorage.setItem('selectedWorkshop', JSON.stringify(workshopData));
        });
    });

    // 2. Logic for booking-calendar.html
    if (document.getElementById('calendar-days-grid')) {
        const workshop = JSON.parse(localStorage.getItem('selectedWorkshop'));
        if (!workshop) {
            const availabilityPanel = document.querySelector('.availability-panel');
            if (availabilityPanel) {
                availabilityPanel.innerHTML = '<h3>No Workshop Selected</h3><p>Please <a href="/workshops/">go back to the workshops page</a> and select a workshop to book.</p>';
            }
            return;
        }

        const monthYearDisplay = document.getElementById('month-year-display');
        const daysGrid = document.getElementById('calendar-days-grid');
        const prevMonthBtn = document.getElementById('prev-month-btn');
        const nextMonthBtn = document.getElementById('next-month-btn');
        const availabilitySlots = document.getElementById('availability-slots');
        const serviceDetailsSection = document.getElementById('service-details-section');
        const nextButton = document.getElementById('next-button');

        let currentDate = new Date(2025, 6, 1); // Start in July 2025 for demo
        let selectedDate = null;
        let selectedTime = null;

        const availabilityData = {
            "2025-07-09": ["10:00 AM", "11:00 AM", "02:00 PM"],
            "2025-07-14": ["03:00 PM"],
            "2025-07-16": ["10:00 AM", "11:00 AM"],
            "2025-07-21": ["04:00 PM"],
            "2025-07-23": ["10:00 AM"],
            "2025-07-28": ["11:00 AM"],
            "2025-07-30": ["02:00 PM"],
            "2025-08-05": ["10:00 AM", "11:00 AM"],
        };
        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

        const renderCalendar = () => {
            const year = currentDate.getFullYear();
            const month = currentDate.getMonth();
            monthYearDisplay.textContent = `${monthNames[month]} ${year}`;
            daysGrid.innerHTML = '';
            
            const firstDayOfMonth = new Date(year, month, 1).getDay();
            const lastDateOfMonth = new Date(year, month + 1, 0).getDate();
            
            for (let i = 0; i < firstDayOfMonth; i++) {
                daysGrid.innerHTML += `<div class="day other-month"></div>`;
            }
            
            for (let i = 1; i <= lastDateOfMonth; i++) {
                const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`;
                let classes = 'day';
                if (availabilityData[dateStr]) classes += ' available';
                if(selectedDate && selectedDate.getDate() === i && selectedDate.getMonth() === month) {
                    classes += ' selected';
                }
                daysGrid.innerHTML += `<div class="${classes}" data-date="${i}">${i}</div>`;
            }
        };

        const updateAvailabilityPanel = (date) => {
            selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), date);
            const dateStr = `${selectedDate.getFullYear()}-${String(selectedDate.getMonth() + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
            const dayName = selectedDate.toLocaleDateString('en-US', { weekday: 'long' });
            
            document.getElementById('availability-title').innerHTML = `Availability for ${dayName}, ${monthNames[selectedDate.getMonth()]} ${date}`;
            
            const times = availabilityData[dateStr];
            if (times && times.length > 0) {
                availabilitySlots.innerHTML = times.map(time => `<button class="time-slot" data-time="${time}">${time}</button>`).join('');
            } else {
                availabilitySlots.innerHTML = `<p class="availability-placeholder">No availability for this date.</p>`;
            }
        };
        
        const resetSelection = () => {
             selectedDate = null;
             selectedTime = null;
             nextButton.disabled = true;
             serviceDetailsSection.classList.add('hidden');
             availabilitySlots.innerHTML = '<p class="availability-placeholder">Please select a date to see availability.</p>';
             document.querySelectorAll('.day.selected').forEach(d => d.classList.remove('selected'));
        }

        daysGrid.addEventListener('click', (e) => {
            if (e.target.classList.contains('day') && !e.target.classList.contains('other-month') && e.target.classList.contains('available')) {
                document.querySelectorAll('.day.selected').forEach(d => d.classList.remove('selected'));
                e.target.classList.add('selected');
                updateAvailabilityPanel(parseInt(e.target.dataset.date, 10));
                
                // Reset time selection
                selectedTime = null;
                nextButton.disabled = true;
                serviceDetailsSection.classList.add('hidden');
            }
        });

        availabilitySlots.addEventListener('click', (e) => {
            if (e.target.classList.contains('time-slot')) {
                document.querySelectorAll('.time-slot.selected').forEach(ts => ts.classList.remove('selected'));
                e.target.classList.add('selected');
                selectedTime = e.target.dataset.time;
        
                const formattedDate = selectedDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
                // document.getElementById('service-name-details').textContent = workshop.name;
                document.getElementById('service-price-details').textContent = workshop.price;
                document.getElementById('service-datetime-details').textContent = `${formattedDate} at ${selectedTime}`;
                document.getElementById('service-duration-details').textContent = workshop.duration;
                
                serviceDetailsSection.classList.remove('hidden');
                nextButton.disabled = false;
            }
        });

        nextButton.addEventListener('click', () => {
            if (workshop && selectedDate && selectedTime) {
                const bookingDetails = {
                    ...workshop,
                    date: selectedDate.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }),
                    time: selectedTime
                };
                localStorage.setItem('bookingDetails', JSON.stringify(bookingDetails));
                window.location.href = '/booking-form/';
            }
        });

        prevMonthBtn.addEventListener('click', () => { currentDate.setMonth(currentDate.getMonth() - 1); renderCalendar(); resetSelection(); });
        nextMonthBtn.addEventListener('click', () => { currentDate.setMonth(currentDate.getMonth() + 1); renderCalendar(); resetSelection(); });
        
        renderCalendar();
    }

    // 3. Logic for booking-form.html
    if (document.querySelector('.booking-form-layout')) {
        const bookingDetails = JSON.parse(localStorage.getItem('bookingDetails'));
        if (bookingDetails) {
            document.getElementById('summary-service-name').textContent = bookingDetails.name;
            document.getElementById('summary-date-time').textContent = `${bookingDetails.date}, ${bookingDetails.time}`;
            document.getElementById('summary-price').textContent = bookingDetails.price;
        } else {
            // If user lands here without booking details, redirect them
            window.location.href = '/workshops/';
        }
    }
});