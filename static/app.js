document.getElementById("chatForm").onsubmit = async (e) => {
  e.preventDefault();

  let formData = new FormData(e.target);
  console.log(formData);

  let loader = document.getElementById("loader");
  loader.style.display = "block";

  let response = await fetch("/ask", {
    method: "POST",
    body: formData,
  });

  let data = await response.json();

  let ans = document.getElementById("answer");
  ans.innerText = data.response;

  loader.style.display = "none";
  document.getElementById("inp").value = "";
};
