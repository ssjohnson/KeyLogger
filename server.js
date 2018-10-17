const FtpSrv = require('ftp-srv');
const ftpServer = new FtpSrv('ftp://127.0.0.1:5555', { greeting : "Hello World" });

ftpServer.on('login', ({connection, username, password}, resolve, reject) => {
    console.log("Login from: " + connection.ip);
    console.log("Username:" + username);
    if(username == 'root' && password == 'root'){
        console.error("resolving");
        resolve({root: '/Users/Stephen/Desktop/project/keylogger/', cwd : '/ftpserver/root/'});
    } else {
        reject("Connection Refused");
    }
});

ftpServer.on('client-error', ({connection, context, error}) => {
    console.error("CLIENT ERROR:");
    console.error("CONTEXT : " + context);
    console.error("ERROR: " + error);
    connection.close();
});

ftpServer.on('STOR', (error, filename) => {
    if(error) {
        console.error("ERROR UPLOADING FILE: " + filename);
    }
});

ftpServer.listen()
.then(() => {});