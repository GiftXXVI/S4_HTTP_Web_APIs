load_interests = function () {
  fetch("http://localhost:8080/interests", {
    method: "GET",
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (jsonResponse) {
      console.log(jsonResponse);
      document.getElementById("interests").innerHTML = "";
      for (let ind = 0; ind < jsonResponse["interests"].length; ind++) {
        const liItem = document.createElement("LI");
        liItem.className = "list-group-item";

        liItem.dataset.id = jsonResponse["interests"][ind]["id"];
        liItem.dataset.name = jsonResponse["interests"][ind]["name"];
        var modify = document.createElement("a");
        var remove = document.createElement("a");
        var modifyIcon = document.createElement("i");
        modifyIcon.className = "bi bi-pen";
        var removeIcon = document.createElement("i");
        removeIcon.className = "bi bi-trash";
        modify.appendChild(modifyIcon);
        remove.appendChild(removeIcon);

        modify.title = "Edit";
        modify.href = "";
        modify.dataset.id = liItem.dataset.id;
        modify.dataset.name = liItem.dataset.name;
        modify.className = "btn btn-sm btn-secondary mx-2";

        remove.title = "Delete";
        remove.href = "";
        remove.dataset.id = liItem.dataset.id;
        remove.className = "btn btn-sm btn-danger";

        liItem.innerHTML = jsonResponse["interests"][ind]["name"];
        liItem.appendChild(modify);
        liItem.appendChild(remove);
        document.getElementById("interests").appendChild(liItem);
        console.log(remove)
      }
    });
};

window.onload = load_interests;

document.getElementById("interest_form").onsubmit = function (e) {
  e.preventDefault();

  fetch("http://localhost:8080/interests", {
    method: "POST",
    body: JSON.stringify({
      name: document.getElementById("name").value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (jsonResponse) {
      console.log(jsonResponse);
      if (jsonResponse["success"] == true) {
        load_interests();
        document.getElementById("name").value = "";
      } else {
        console.log("An Error Occurred!");
      }

      //window.location.reload(true);
    });
};
