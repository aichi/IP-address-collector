var ip = require('ip');
var azure = require('azure-storage');
var osenv = require('osenv');
var Guid = require('guid');

//console.log(process.env.AZURE_STORAGE_ACCOUNT);
//console.log(process.env.AZURE_STORAGE_ACCESS_KEY);

// Some things are not reliably in the env, and have a fallback command:
var h = osenv.hostname(function (er, hostname) {
    h = hostname
});

var localIpAddress = ip.address();
var tableSvc = azure.createTableService();


osenv.hostname(function (error, hostname) {
    if (!error) {
        var localIp = {
            PartitionKey: {'_':'localIp'},
            RowKey: {'_': '' + Guid.create()},
            ip: {'_': localIpAddress},
            hostName: {'_': hostname}
        };

        tableSvc.createTableIfNotExists('deviceip', function(error, result, response){
            if(!error){
                tableSvc.insertEntity('deviceip',localIp, function (error, result, response) {
                    if(!error){
                        console.log('IP address: ' + JSON.stringify(localIp) + 'saved to Azure');
                    } else {
                        console.log(error);
                    }
                });
            } else {
                console.log(error);
            }
        });
    } else {
        console.log(error);
    }
});





