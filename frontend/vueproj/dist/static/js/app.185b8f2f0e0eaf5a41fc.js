webpackJsonp([1],{0:function(e,n){},NHnr:function(e,n,o){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var t=o("7+uW"),a={render:function(){var e=this.$createElement,n=this._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},staticRenderFns:[]};var r=o("VU/8")({name:"App"},a,!1,function(e){o("gsu9")},null,null).exports,l=o("/ocq"),c=o("fZjL"),s=o.n(c),u=o("BO1k"),i=o.n(u),d=o("6zY2"),f=o.n(d),v=o("DmT9"),p=o.n(v),m={name:"app",components:{wordcloud:f.a},created:function(){var e=this;console.log("myColors is: "+this.myColors);var n=p()("http://127.0.0.1:5000");n.on("connect",function(){console.log("--- connect -----"),n.emit("test_connect",{data:"I'm connected!"})}),n.on("connected",function(){console.log("connected")}),n.on("wordStats_msg",function(n){console.log("---------- wordStats_msg event data --------"),console.log(n);var o=JSON.parse(n.data);console.log(o);var t=[],a=!0,r=!1,l=void 0;try{for(var c,u=i()(o);!(a=(c=u.next()).done);a=!0){var d=c.value,f=s()(d)[0],v=d[f];t.push({name:f,value:v})}}catch(e){r=!0,l=e}finally{try{!a&&u.return&&u.return()}finally{if(r)throw l}}console.log(t),e.defaultWords.splice(0);var p=!0,m=!1,h=void 0;try{for(var w,g=i()(t);!(p=(w=g.next()).done);p=!0){var y=w.value;e.defaultWords.push(y)}}catch(e){m=!0,h=e}finally{try{!p&&g.return&&g.return()}finally{if(m)throw h}}}),n.on("disconnect",function(){console.log("--- disconnect -----")})},methods:{wordClickHandler:function(e,n,o){console.log("wordClickHandler",e,n,o)}},data:function(){return{myColors:["#1f77b4","#629fc9","#94bedb","#c9e0ef"],defaultWords:[{name:"Cat",value:26},{name:"fish",value:19},{name:"things",value:18},{name:"look",value:16},{name:"two",value:15},{name:"fun",value:9},{name:"know",value:9},{name:"good",value:9},{name:"play",value:6}]}}},h={render:function(){var e=this.$createElement,n=this._self._c||e;return n("div",{attrs:{id:"app"}},[n("wordcloud",{attrs:{data:this.defaultWords,nameKey:"name",valueKey:"value",color:this.myColors,showTooltip:!0,wordClick:this.wordClickHandler}})],1)},staticRenderFns:[]},w=o("VU/8")(m,h,!1,null,null,null).exports;t.a.use(l.a);var g=new l.a({routes:[{path:"/",name:"WordCloud",component:w}]});t.a.config.productionTip=!1,new t.a({el:"#app",router:g,components:{App:r},template:"<App/>"})},gsu9:function(e,n){}},["NHnr"]);
//# sourceMappingURL=app.185b8f2f0e0eaf5a41fc.js.map