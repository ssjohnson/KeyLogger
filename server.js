const FtpSrv = require('ftp-srv');
const ftpServer = new FtpSrv('ftp://127.0.0.1:55555', {});
const fs = require('fs');
const pathExists = require('path-exists');
var dirPath = '/ftpserver/root/';

ftpServer.on('login', ({connection, username, password}, resolve, reject) => {
    console.log("Login from: " + connection.ip);
    console.log("Username:" + username);
    if(username == 'root' && password == 'root'){
        console.log("Resolving");
        resolve({ root: __dirname, cwd : dirPath});
    } else {
        reject("Connection Refused");
    }
});

ftpServer.on('client-error', ({connection, context, error}) => {
    console.error("CLIENT ERROR:");
    console.error("CONTEXT : " + context);
    console.error(error.stack);
});

ftpServer.on('STOR', (error, filename) => {
    if(error) {
        console.error("ERROR UPLOADING FILE: " + filename);
    } else {
        console.log("Successfully Uploaded: " + filename)
    }
});

ftpServer.listen().then(() => {
    pathExists('./ftpserver/').then(exists => {
        console.log(exists);
        if(exists) {
            pathExists('./ftpserver/root').then(exists => {
                if(exists) console.log("File Directories Exist");
                else {
                    fs.mkdirSync('./ftpserver/root/', (err) => {
                        if(err) throw err;
                    });
                }
            });
        }
        else {
            fs.mkdirSync('./ftpserver/', (err) => {
                if(err) throw err;
            });
            fs.mkdirSync('./ftpserver/root/', (err) => {
                if(err) throw err;
            });
        }
    });
});