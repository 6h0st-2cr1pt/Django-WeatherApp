document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.querySelector('.temperature');
    const feelsLikeElement = document.querySelector('.feels-like');
    const tempMaxElement = document.querySelector('.temp-max');
    const tempMinElement = document.querySelector('.temp-min');
    const unitButtons = document.querySelectorAll('[data-unit]');
    const citySearchForm = document.getElementById('citySearchForm');

    function celsiusToFahrenheit(celsius) {
        return (celsius * 9/5) + 32;
    }

    function fahrenheitToCelsius(fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    function updateTemperature(element, celsius, unit) {
        let temperature = parseFloat(celsius);
        if (unit === 'F') {
            temperature = celsiusToFahrenheit(temperature);
        }
        element.textContent = `${temperature.toFixed(1)}°${unit}`;
    }

    function updateAllTemperatures(unit) {
        const elements = [
            { el: temperatureElement, celsius: parseFloat(temperatureElement.dataset.celsius) },
            { el: feelsLikeElement, celsius: parseFloat(feelsLikeElement.dataset.celsius) },
            { el: tempMaxElement, celsius: parseFloat(tempMaxElement.dataset.celsius) },
            { el: tempMinElement, celsius: parseFloat(tempMinElement.dataset.celsius) }
        ];

        elements.forEach(item => updateTemperature(item.el, item.celsius, unit));
    }

    unitButtons.forEach(button => {
        button.addEventListener('click', function() {
            const unit = this.dataset.unit;
            updateAllTemperatures(unit);
            unitButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });

    citySearchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        this.submit();
    });
    updateAllTemperatures('C');
});

