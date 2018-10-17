const FtpSrv = require('ftp-srv');
const ftpServer = new FtpSrv('ftp://127.0.0.1:5555', {greeting:"Hello World"});

ftpServer.on('login', (data, resolve, reject) => {});

ftpServer.listen()
.then(() => {});