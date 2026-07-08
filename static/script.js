document.addEventListener('DOMContentLoaded', function () {

    const loanForm = document.getElementById('loanForm');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');

    const resultStatus = document.getElementById('resultStatus');
    const confidence = document.getElementById('confidence');
    const probability = document.getElementById('probability');

    const errorMessage = document.getElementById('errorMessage');

    const heroDecision = document.getElementById('heroDecision');
    const heroSummary = document.getElementById('heroSummary');

    const submitButton = document.querySelector('.btn-submit');


    // ============================================================
    // VALIDATE FORM DATA
    // ============================================================

    function validateFormData(data) {

        const applicantIncome =
            parseFloat(data.ApplicantIncome);

        const coapplicantIncome =
            parseFloat(data.CoapplicantIncome);

        const loanAmount =
            parseFloat(data.LoanAmount);

        const loanTerm =
            parseFloat(data.Loan_Amount_Term);


        return (

            data.Gender !== '' &&

            data.Married !== '' &&

            data.Dependents !== '' &&

            data.Education !== '' &&

            data.Self_Employed !== '' &&

            data.Credit_History !== '' &&

            data.Property_Area !== '' &&


            !Number.isNaN(applicantIncome) &&

            applicantIncome >= 0 &&


            !Number.isNaN(coapplicantIncome) &&

            coapplicantIncome >= 0 &&


            !Number.isNaN(loanAmount) &&

            loanAmount > 0 &&


            !Number.isNaN(loanTerm) &&

            loanTerm > 0

        );
    }


    // ============================================================
    // DISPLAY PREDICTION RESULT
    // ============================================================

    function displayResult(result) {

        const approved =
            result.prediction === 'Loan Approved';


        // Backend already sends percentage value
        // Example: 41.37, NOT 0.4137

        const approvalProbability =
            Number(result.approval_probability);


        // --------------------------------------------------------
        // DISPLAY APPROVED / REJECTED
        // --------------------------------------------------------

        resultStatus.className =

            `result-status ${
                approved
                    ? 'approved'
                    : 'rejected'
            }`;


        resultStatus.textContent =

            approved
                ? 'Approved'
                : 'Rejected';


        // --------------------------------------------------------
        // DISPLAY PREDICTION CONFIDENCE
        // --------------------------------------------------------

        confidence.textContent =

            result.confidence || 'N/A';


        // --------------------------------------------------------
        // DISPLAY APPROVAL PROBABILITY
        // --------------------------------------------------------

        if (!Number.isNaN(approvalProbability)) {

            probability.textContent =

                `${approvalProbability.toFixed(2)}%`;

        }

        else {

            probability.textContent = 'N/A';

        }


        // --------------------------------------------------------
        // SHOW RESULT
        // --------------------------------------------------------

        resultSection.style.display = 'block';

        errorSection.style.display = 'none';


        // --------------------------------------------------------
        // UPDATE HERO MODEL STATUS
        // --------------------------------------------------------

        if (heroDecision) {

            heroDecision.textContent =
                result.prediction;

        }


        if (heroSummary) {

            heroSummary.textContent =

                `Approval probability: ${
                    approvalProbability.toFixed(2)
                }%. Prediction confidence: ${
                    result.confidence
                }.`;

        }


        // --------------------------------------------------------
        // SCROLL TO RESULT
        // --------------------------------------------------------

        resultSection.scrollIntoView({

            behavior: 'smooth',

            block: 'nearest'

        });

    }


    // ============================================================
    // DISPLAY ERROR
    // ============================================================

    function displayError(message) {

        resultSection.style.display =
            'none';


        errorSection.style.display =
            'block';


        errorMessage.textContent =
            message;


        if (heroDecision) {

            heroDecision.textContent =
                'Prediction unavailable';

        }


        if (heroSummary) {

            heroSummary.textContent =

                'Please review the applicant details and try again.';

        }

    }


    // ============================================================
    // FORM SUBMISSION
    // ============================================================

    loanForm.addEventListener(

        'submit',

        async function (event) {

            event.preventDefault();


            resultSection.style.display =
                'none';


            errorSection.style.display =
                'none';


            const originalText =

                submitButton.textContent;


            submitButton.disabled =
                true;


            submitButton.textContent =
                'Analyzing Application...';


            try {


                // ------------------------------------------------
                // COLLECT FORM DATA
                // ------------------------------------------------

                const formData =

                    new FormData(
                        loanForm
                    );


                const payload =

                    Object.fromEntries(

                        formData.entries()

                    );


                console.log(

                    'Applicant Data:',

                    payload

                );


                // ------------------------------------------------
                // VALIDATE FORM DATA
                // ------------------------------------------------

                if (

                    !validateFormData(
                        payload
                    )

                ) {

                    throw new Error(

                        'Please fill all required fields with valid values.'

                    );

                }


                // ------------------------------------------------
                // SEND DATA TO FLASK
                // ------------------------------------------------

                const response =

                    await fetch(

                        '/predict',

                        {

                            method: 'POST',


                            headers: {

                                'Content-Type':
                                    'application/json'

                            },


                            body:

                                JSON.stringify(
                                    payload
                                )

                        }

                    );


                // ------------------------------------------------
                // RECEIVE FLASK RESPONSE
                // ------------------------------------------------

                const result =

                    await response.json();


                console.log(

                    'Prediction Result:',

                    result

                );


                // ------------------------------------------------
                // CHECK RESPONSE
                // ------------------------------------------------

                if (

                    !response.ok ||

                    !result.success

                ) {

                    throw new Error(

                        result.message ||

                        'Prediction request failed.'

                    );

                }


                // ------------------------------------------------
                // DISPLAY RESULT
                // ------------------------------------------------

                displayResult(
                    result
                );

            }


            catch (error) {


                console.error(

                    'Prediction Error:',

                    error

                );


                displayError(

                    error.message ||

                    'Prediction failed.'

                );

            }


            finally {


                submitButton.disabled =
                    false;


                submitButton.textContent =
                    originalText;

            }

        }

    );


    // ============================================================
    // CHECK FLASK BACKEND HEALTH
    // ============================================================

    fetch('/health')

        .then(

            response =>
                response.json()

        )

        .then(

            data => {


                if (

                    heroSummary &&

                    data.status === 'ok' &&

                    data.model_loaded

                ) {

                    heroSummary.textContent =

                        'Backend connected and machine learning model ready for prediction.';

                }


                else if (heroSummary) {

                    heroSummary.textContent =

                        'Backend connected, but the machine learning model is not loaded.';

                }

            }

        )

        .catch(

            error => {


                console.error(

                    'Health Check Error:',

                    error

                );


                if (heroSummary) {

                    heroSummary.textContent =

                        'Backend is currently unavailable.';

                }

            }

        );

});