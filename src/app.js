const fs = require('fs');
const { exec } = require('child_process');

process.stdin.setEncoding('utf8');

function generateRandomString(length) {
    const charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        result += charset[randomIndex];
    }
    return result;
}

process.stdout.write('Enter channel link: ');

process.stdin.on('data', function(data) {
    const link = data.trim();
    const file = generateRandomString('6') + '.tmp'
    fs.writeFile(file, link, function(err) {
        if (err) {
            console.error('Error writing to file:', err);
        } else {
            console.log('Data has been written to', file);
        }
    });
    process.exit()
});