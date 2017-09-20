function start() {
    ws = new WebSocket('ws://' + window.location.host + '/ws/');
    main = document.getElementById('main');

    ws.onmessage = function (text) {
        main.innerHTML = text.data
    };
    ws.onclose = function (p1) {
        ws.close()
    };
}
start();