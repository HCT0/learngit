function adding_comment(ev)
{
    var x=document.getElementById("comment-submit-area");
    var y=document.getElementById("comment-submit-area-body");
    x.style.zIndex=1;
    x.style.display="block";
    y.style.zIndex=1;
    y.style.display="block";
}
function unsure(ev)
{
    var x=document.getElementById(ev);
    var y=document.getElementById("comment-submit-area-body");
    x.style.display="none";
    y.style.display="none"
}