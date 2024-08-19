document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova is now initialized');
    document.getElementById('deviceready').classList.add('ready');
}

function fetchBibleVerse() {
    const book = document.getElementById('book').value;
    const chapter = document.getElementById('chapter').value;

    if (!book || !chapter) {
        alert('Please enter both book and chapter.');
        return;
    }

    const apiUrl = `https://www.abibliadigital.com.br/api/verses/nvi/${book}/${chapter}`;

    console.log('Fetching Bible verses from:', apiUrl);

    fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        console.log('Response status:', response.status);
        return response.json();
    })
    .then(data => {
        console.log('Data received from API:', data);
        displayBibleVerse(data);
    })
    .catch(error => {
        console.error('Error fetching the Bible verse:', error);
    });
}

function displayBibleVerse(data) {
    console.log('Displaying Bible verses:', data.verses);
    const verseContainer = document.getElementById('bible-verse');
    if (verseContainer) {
        verseContainer.innerHTML = ''; // Limpa qualquer conteúdo existente
        if (data && data.verses && Array.isArray(data.verses)) {
            data.verses.forEach(verse => {
                const verseElement = document.createElement('p');
                verseElement.textContent = `${verse.number}: ${verse.text}`;
                verseContainer.appendChild(verseElement);
            });
        } else {
            console.error('Invalid data structure:', data);
        }
    } else {
        console.error('Element with ID "bible-verse" not found');
    }
}
