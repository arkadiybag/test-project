function start() {
    ws = new WebSocket('ws://127.0.0.1/ws/');
    main = document.getElementById('main');

    ws.onmessage = function (text) {
        main.innerHTML = text.data
    };
    ws.onclose = function (p1) {
        ws.close()
    };
}
start();