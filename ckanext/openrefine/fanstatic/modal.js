$(document).ready(function () {
  console.log("registando funcion");
  $("#openrefine").click(function () {
    console.log("abriendo");
    window.open($("#openrefine").attr("url"));
  });
});
