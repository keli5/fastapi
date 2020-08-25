const thisPage = window.location.pathname.split('/')[1];
const headerChunk = document.getElementById(thisPage)
headerChunk.className = headerChunk.className + " active"