const express = require('express');
const cors = require('cors');

const app = express();

// Middleware for JSON body parsing
app.use(express.json());
// Middleware for your custom text type
app.use(express.text({ type: 'application/gusp' }));

// app.use(cors({
//     origin: 'http://edu-ctf.zoolab.org:10010',
//     methods: ['GET', 'POST']
// }));

app.use(cors());

const aliasStorage = new Map([
    ['qwe', 'qwe']
]);

const generateAlias = () => {
    let alias = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 8; i++) { // generating 8-character alias, can be adjusted
        alias += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return alias;
};

app.post('/', (req, res) => {
    // console.log("Received request with body:", req.body);
    const match = req.body.match(/\[gusp\]URL\|(\d+)\|([^|]+)(?:\|([^[]+))?\[\/gusp\]/);
    if (match) {
        const [, expectedLength, originalUrl, providedAlias] = match;
        
        if (providedAlias && aliasStorage.has(providedAlias)) {
            res.setHeader('Content-Type', 'application/gusp');
            res.status(400).send(`[gusp]ERROR|0|[/gusp]`);
            return;
        }

        let actualAlias = providedAlias || generateAlias();

        // In case generated alias is already in use, generate a new one
        while (aliasStorage.has(actualAlias)) {
            actualAlias = generateAlias();
        }

        if (expectedLength == originalUrl.length) {
            aliasStorage.set(actualAlias, originalUrl);
            res.setHeader('Content-Type', 'application/gusp');
            res.send(`[gusp]SUCCESS|${actualAlias.length}|${actualAlias}[/gusp]`);
        } else {
            res.setHeader('Content-Type', 'application/gusp');
            res.status(400).send(`[gusp]ERROR|0|[/gusp]`);
        }
    } else {
        res.setHeader('Content-Type', 'application/gusp');
        res.status(400).send(`[gusp]ERROR|0|[/gusp]`);
    }
});

app.get('/', (req, res) => {
    res.send('API server is up and running');
});

app.get('/:alias', (req, res) => {
    if (aliasStorage.has(req.params.alias)) {
        res.redirect(302, aliasStorage.get(req.params.alias));
    } else {
        res.status(404).send('Alias not found');
    }
});

app.post('/submit_flag', (req, res) => {
    try {
        console.log("Received request with body:", req.body);
        const payload = JSON.parse(req.body.toString('utf-8'));
        const flag = payload.flag;
        if (flag) {
            console.log(`Received flag: ${flag}`);
            // Respond with the received flag
            res.json({ "message": `Flag received: ${flag}` });
        } else {
            res.status(400).json({ "message": "Flag not found in payload" });
        }
    } catch (err) {
        res.status(400).json({ "message": "Invalid JSON payload" });
    }
});

app.listen(4000, () => {
    console.log('API server is running on port 4000');
});
