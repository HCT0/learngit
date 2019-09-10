	function topfunction(ev)
	{	
		var x=document.getElementById(ev);
		if (x.style.display=="none") 
		{
			x.style.display="block";
			if(ev=="bloger")
			{	
				var c=document.getElementById("left");
				c.style.transform='rotate(180deg)';
				c.style.left="15%";
				x.style.position="absolute";
				x.style.left="-15%";
				x.style.top="20%";
				var sum=0;	
				var timer=setInterval(function ()
				{
					sum++;
					var x=document.getElementById("bloger").style.left;
					var y=document.getElementById("bloger");
					//console.log(parseInt(x));
					x=parseInt(x)+0.01+"%";
					y.style.left=x;
					if (sum==16)
					{	
						sum=0;
						clearInterval(timer);
					}			
				},20);
			}
			else if(ev=="catelog")
			{	
				var c=document.getElementById("right");
				c.style.transform='rotate(180deg)';
				c.style.right="15%";
				x.style.position="absolute";
				x.style.right="-15%";
				x.style.top="20%"
				var sum=0;	
				var timer=setInterval(function ()
				{
					sum++;
					var x=document.getElementById("catelog").style.right;
					var y=document.getElementById("catelog");
					//console.log(parseInt(x));
					x=parseInt(x)+0.01+"%";
					y.style.right=x;
					if (sum==16)
					{	
						sum=0;
						clearInterval(timer);
					}			
				},20);
			}
			else if(ev=="front")
			{	
				var c=document.getElementById("top");
				c.style.transform='rotate(180deg)';
				c.style.top="15%";
				x.style.position="absolute";
				x.style.left="0%";
				x.style.top="-15%";
				var sum=0;	
				var timer=setInterval(function ()
				{
					sum++;
					var x=document.getElementById("front").style.top;
					var y=document.getElementById("front");
					//console.log(parseInt(x));
					x=parseInt(x)+0.01+"%";
					y.style.top=x;
					if (sum==16)
					{	
						sum=0;
						clearInterval(timer);
					}			
				},20);
			}
			else if(ev=="footer")
			{
				{	
					var c=document.getElementById("bottom");
					c.style.zIndex=2;
					c.style.transform='rotate(180deg)';
					c.style.bottom="75%";

					x.style.position="absolute";
					x.style.left="5%";
					x.style.bottom="-90%";
					x.style.zIndex=1;
					
					var sum=0;	
					var timer=setInterval(function ()
					{
						sum++;
						var x=document.getElementById("footer").style.bottom;
						var y=document.getElementById("footer");
						//console.log(parseInt(x));
						x=parseInt(x)+0.01+"%";
						y.style.bottom=x;
						if (sum==76)
						{	
							sum=0;
							clearInterval(timer);
						}			
					},1);
				}
				
			}

		}
		else//这个是设定在收缩的时候，箭头转向
		{
			x.style.display="none";//先将内容隐藏
			if(ev=="bloger")
			{
				var c=document.getElementById("left");
				c.style.transform='rotate(0deg)';
				c.style.left="10%";
			}
			else if(ev=="catelog")
			{
				var c=document.getElementById("right");
				c.style.transform='rotate(0deg)';
				c.style.right="10%";
			}
			else if(ev=="front")
			{
				var c=document.getElementById("top");
				c.style.top="5%";
				c.style.transform='rotate(0deg)';	
			}
			else if(ev=="footer")
			{
				var c=document.getElementById("bottom");
				c.style.bottom="5%";
				c.style.transform='rotate(0deg)';
			}

		}
		
	}

	function pre_page(ev)//在这里进行换页操作
	{
		var x=document.getElementById("page-first").innerHTML;
		if(x==1)
			{
				alert("这已经是第一页咯！");
			}
		else
			{

				console.log("在这里执行换页操作");
			}

	}

	function page_head(ev)
	{
		var x=document.getElementById("page-first").innerHTML;
		if(x==1)//first是第一页，不要进行换页操作
		{
			alert("这已经是首页啦!");
		}
		else//first不是第一页，则要进行展示第一页操作
		{
			console.log("在这里执行进入第一页操作");
		}
	}
	function next_page()
	{
		//x代表总页数
		var x=document.getElementById("all-page").innerHTML;
		if(x==1)//只有一页的情况
		{
			alert("这已经是最后一页");
		}
		else if(x==2)//有两页的情况
		{
			var y=document.getElementById("page-first").innerHTML;
			if(y==x)//first是最后一页
			{
				alert("这已经是最后一页");
			}
			else//first不是最后一页，则进行换页操作
			{
				document.getElementById("page-first").innerHTML=++y;
				//执行数据库的换页
				
				$.ajax({
					url :'/myblog_2/',
					type:'POST',
					data : { "page" : 2 },

					success:function(all)
					{
						console.log(all);
						for (i=0;i<10;i++)
							{
							console.log(all[i])
							}
						//var f=document.getElementById("footer-a");
						//document.getElementById("f-title").innerHTML=all.title;
		

						/*var n=f.nextSibling;
						for ( var i=0;i<7;i++)//向将前一页的内容隐藏
						{
							f.style.display="none";
							f=n.nextSibling;
							n=f.nextSibling;
						}*/


					},
					error:function(all){
						alert("进入失败");
					}		
				})
			}
		}
		else if(x==3)//有三页的情况
		{
			var y=document.getElementById("page-first").innerHTML;
			if(x==y)//first是第一页
			{
				alert("这已经是最后一页");
			}
			else//first不是第一页，则进行换页操作
			{
				y++;
				console.log("在这里执行加页操作");
			}
		}

	}

	function last_page()
	{
		var x=document.getElementById("all-page").innerHTML;
		x=parseInt(x);
		var y=document.getElementById("page-first").innerHTML;
		if(x==y)//first已经是最后一页，就不要进行换页操作
		{
			alert("本页已经是最后一页");
		}
		else//first不是最后一页，进行直接进入最后一页的操作
		{
			console.log("在这里执行进入最后一页操作");
		}

	}
