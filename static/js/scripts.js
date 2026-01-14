/*!
* Start Bootstrap - Clean Blog v6.0.5
* https://startbootstrap.com/theme/clean-blog
*/

// ==========================
// NAVBAR SCROLL LOGIC (KEEP)
// ==========================
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav ? mainNav.clientHeight : 0;

    window.addEventListener('scroll', function () {
        const currentTop = document.body.getBoundingClientRect().top * -1;

        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav?.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav?.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav?.classList.remove('is-visible');
            if (currentTop > headerHeight && !mainNav?.classList.contains('is-fixed')) {
                mainNav?.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
});


// ==========================
// ML PREDICTION LOGIC (ADD)
// ==========================
async function predictWineQuality() {
    try {
        // Read input values from form
        const data = {
            fixed_acidity: document.getElementById("fixed_acidity").value,
            volatile_acidity: document.getElementById("volatile_acidity").value,
            citric_acid: document.getElementById("citric_acid").value,
            residual_sugar: document.getElementById("residual_sugar").value,
            chlorides: document.getElementById("chlorides").value,
            free_sulfur_dioxide: document.getElementById("free_sulfur_dioxide").value,
            total_sulfur_dioxide: document.getElementById("total_sulfur_dioxide").value,
            density: document.getElementById("density").value,
            pH: document.getElementById("pH").value,
            sulphates: document.getElementById("sulphates").value,
            alcohol: document.getElementById("alcohol").value
        };

        // Call Render backend API
        const response = await fetch(
            "https://wine-quality-ml-project.onrender.com", // 🔴 CHANGE to your Render URL
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        // Display prediction
        document.getElementById("predictionResult").innerText =
            "Predicted Wine Quality: " + result.prediction;

    } catch (error) {
        console.error(error);
        document.getElementById("predictionResult").innerText =
            "Error predicting wine quality";
    }
}
