//Javascript file to copy Url Link of current page

const copyBtn = document.getElementById('copyURL');

        copyBtn.addEventListener('click', () => {
            const url = window.location.href;  // Get the current page URL
            navigator.clipboard.writeText(url)  // Write URL to clipboard
                .then(() => {
                    alert('URL copied successfully!');
                })
                .catch(() => {
                    alert('Error copying URL to clipboard');
                });
        });


