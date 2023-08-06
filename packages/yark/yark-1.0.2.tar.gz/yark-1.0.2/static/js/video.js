// Creates note by fetching to the api
function createNote(el) {
    // Get top class
    let top = el.getElementsByClassName("top")[0]

    // Get title
    let title = top.getElementsByClassName("title")[0].innerText
    if (title == "") {
        addError("No title provided for element")
    }

    // Get timestamp
    let timestamp = top.getElementsByClassName("timestamp")[0].innerText

    // Get body and clean
    let body = el.getElementsByClassName("body")[0].innerText
    if (body == "") {
        body = null
    }

    // Send request
    fetch("", {
        method: "PUT",
        body: JSON.stringify({
            title: title, body: body, timestamp: timestamp
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(resp => resp.json().then(json => {
        // Reload at created id
        window.location.href += "#" + json["id"]
        window.location.reload()
    }))
}

// Puts the video player element to the provided timestamp
function toTimestamp(timestamp) {
    let player = document.getElementById("player")
    player.currentTime = Math.abs(timestamp - 1)
    player.play()
}

// Listen for `focusout` event on note title
document.addEventListener("focusout", (event) => {
    let el = event.srcElement
    if ((el.classList.contains("title") || el.classList.contains("body")) && !el.classList.contains("createnote-input")) {
        // Make payload for title
        let payload = {}
        if (el.classList.contains("title")) {
            payload["id"] = el.parentElement.parentElement.getElementsByClassName("id")[0].innerText
            payload["title"] = el.innerText
        } else {
            payload["id"] = el.parentElement.getElementsByClassName("id")[0].innerText
            if (el.innerText == "") {
                payload["body"] = null
            } else {
                payload["body"] = el.innerText
            }
        }

        // Send update
        fetch("", {
            method: "PATCH",
            body: JSON.stringify(
                payload
            ),
            headers: {
                "Content-Type": "application/json"
            }
        })
    }
})

function toggleButton(id, name, caller) {
    let el = document.getElementById(id);
    if (el.style.display === "none" || el.style.display === "") {
        caller.innerText = "Hide " + name;
        el.style.display = "block";
    } else {
        caller.innerText = "Show " + name;
        el.style.display = "none";
    }
}