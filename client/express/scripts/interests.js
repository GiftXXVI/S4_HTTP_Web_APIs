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
        modifyIcon.dataset.id = liItem.dataset.id;
        modifyIcon.dataset.name = liItem.dataset.name;
        var removeIcon = document.createElement("i");
        removeIcon.className = "bi bi-trash";
        removeIcon.dataset.id = liItem.dataset.id;
        removeIcon.dataset.name = liItem.dataset.name;
        modify.appendChild(modifyIcon);
        remove.appendChild(removeIcon);

        modify.title = "Edit";
        modify.href = "";
        modify.id = "modify_interest";
        modify.dataset.id = liItem.dataset.id;
        modify.dataset.name = liItem.dataset.name;
        modify.setAttribute("data-bs-toggle", "modal");
        modify.setAttribute("data-bs-target", "#modifyModal");
        modify.className = "btn btn-sm btn-secondary mx-2";

        remove.title = "Delete";
        remove.href = "";
        modify.id = "delete_interest";
        remove.dataset.id = liItem.dataset.id;
        remove.className = "btn btn-sm btn-danger";

        liItem.innerHTML = jsonResponse["interests"][ind]["name"];
        liItem.appendChild(modify);
        liItem.appendChild(remove);
        document.getElementById("interests").appendChild(liItem);

        modify.onclick = function (e) {
          e.preventDefault();
          data_id = e.target.getAttribute("data-id");
          data_name = e.target.getAttribute("data-name");
          modifyName = document.getElementById("modifyName");
          modifyName.value = data_name;
          modifyName.setAttribute("id", data_id);
        };
        remove.onclick = function (e) {
          e.preventDefault();
          fetch(
            `http://localhost:8080/interests/${e.target.getAttribute(
              "data-id"
            )}`,
            { method: "DELETE" }
          )
            .then(function (response) {
              return response.json();
            })
            .then(function (jsonResponse) {
              load_interests();
            });
        };
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
    });
};

document.getElementById("submitInterest").onclick = function (e) {
  e.preventDefault();
  modifyName = modifyModal.querySelector(".modal-body input");
  console.log(modifyName);
  fetch(`http://localhost:8080/interests/${modifyName.getAttribute("id")}`, {
    method: "PATCH",
    body: JSON.stringify({
      id: modifyName.getAttribute("id"),
      name: modifyName.value,
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
      
    });
};
