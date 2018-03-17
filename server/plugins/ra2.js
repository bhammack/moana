var quotes = [
    'Rockets in the sky.',
    'I can go anywhere!',
    'For the Union.',
    'Rubber shoes in motion.',
    'Kirov reporting.',
    'Helium mix optimal.'
];


module.exports = {
    quote: function() {
        return quotes[Math.floor(Math.random()*quotes.length)];
    }
}