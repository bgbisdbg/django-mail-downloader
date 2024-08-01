$(document).ready(function() {
    var socket = new WebSocket('ws://' + window.location.host + '/ws/email_import/');
    socket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        if (data.type === 'progress') {
            $('#progress-status').text(data.message);
            $('#progress-bar-inner').width(data.progress + '%');
            if (data.progress === 100) {
                $('#progress-status').text('Готово').addClass('completed');
            }
        } else if (data.type === 'message') {
            var message = data.message;
            var row = `<tr>
                <td>${message.subject}</td>
                <td>${message.sent_date}</td>
                <td>${message.received_date}</td>
                <td>${message.body.slice(0, 50)}</td>
                <td>${message.attachments.join(', ')}</td>
            </tr>`;
            $('#message-table-body').append(row);
        }
    };
});