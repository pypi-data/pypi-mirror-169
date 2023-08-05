(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[20],{1424:function(e,t,n){"use strict";n.r(t);var a,i=n(0),c=n.n(i),r=n(255),s=n(11),o=n(18),l=n(2),d=n(13),m=n.n(d),u=n(33),j=n(154),p=n(59),x=n(47),h=n(188),_=n(45),b=n(257),f=Object(b.a)({});function v(){var e=j.a.fetchActivityData(),t=e.call;return{call:function(){return t((function(e){Object(p.a)({detail:e,model:f})})).then((function(e){f.setState({activityData:e})}))},abort:e.abort}}var g=Object(l.a)(Object(l.a)({},f),{},{destroy:function(){f.destroy(),a.abort()},initialize:function(){f.init(),a=v();try{a.call((function(e){Object(p.a)({detail:e,model:f})}))}catch(t){Object(x.a)({notification:{messages:[t.message],severity:"error",id:Date.now()},model:f})}var e="true"===Object(_.a)("askEmailSent");f.setState({askEmailSent:e})},getActivityData:v,onSendEmail:function(e){return fetch("https://formspree.io/f/xeqvdval",{method:"Post",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)}).then(function(){var e=Object(u.a)(m.a.mark((function e(t){return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.json();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()).then((function(e){return e.ok?(Object(x.a)({notification:{severity:"success",messages:["Email Successfully sent"],id:Date.now()},model:f}),f.setState({askEmailSent:!0}),Object(_.b)("askEmailSent",!0)):Object(x.a)({notification:{severity:"error",messages:["Please enter valid email"],id:Date.now()},model:f}),e}))},onHomeNotificationDelete:function(e){Object(h.a)({model:f,id:e})}}),O=n(15),y=n(658),w=n.p+"static/media/github.a1af1e77.svg",N=n.p+"static/media/slack.2d5fba05.svg",C=n(5),S=n(167),k=(n(938),n(1));function E(e){var t=e.title,n=e.path,a=e.description,i=e.icon;return Object(k.jsx)(s.a,{children:Object(k.jsxs)(S.c,{className:"ExploreAimCard",to:"/".concat(n),children:[Object(k.jsx)("div",{className:"ExploreAimCard__icon",children:Object(k.jsx)(C.f,{name:"".concat(i)})}),Object(k.jsx)(C.n,{component:"h4",weight:600,size:16,className:"ExploreAimCard__title",tint:100,children:t}),Object(k.jsx)(C.n,{component:"span",weight:400,size:14,className:"ExploreAimCard__desc",tint:100,children:a}),Object(k.jsx)("div",{className:"ExploreAimCard__arrow__icon",children:Object(k.jsx)(C.f,{name:"long-arrow-right"})})]})})}var D=c.a.memo(E),z=(n(939),[{title:"Runs Explorer",description:"View all your runs holistically on Runs Explorer: all hyperparameters, all metric last values",path:"runs",icon:"runs"},{title:"Metrics Explorer",description:"Compare 100s of metrics in a few clicks on Metrics Explorer",path:"metrics",icon:"metrics"},{title:"Images Explorer",description:"Track intermediate images and search, compare them on Images Explorer",path:"images",icon:"images"},{title:"Params Explorer",description:"The Params explorer enables a parallel coordinates view for metrics and params",path:"params",icon:"params"},{title:"Scatters Explorer",description:"Explore and learn relationship, correlations, and clustering effects between metrics and parameters on Scatters Explorer",path:"scatters",icon:"scatterplot"}]);function A(){return Object(k.jsx)(s.a,{children:Object(k.jsxs)("div",{className:"ExploreAim",children:[Object(k.jsxs)("div",{children:[Object(k.jsx)(C.n,{component:"h2",tint:100,weight:600,size:24,children:"Get Involved"}),Object(k.jsxs)("div",{className:"ExploreAim__social",children:[Object(k.jsxs)("a",{target:"_blank",href:"https://slack.aimstack.io",rel:"noreferrer",className:"ExploreAim__social__item",onClick:function(){return Object(O.b)(o.a.home.slackCommunity)},children:[Object(k.jsx)("img",{src:N,alt:"slack"}),Object(k.jsx)(C.n,{component:"span",tint:100,size:16,weight:400,children:"Join Aim slack community"}),Object(k.jsx)(C.f,{name:"arrow-right"})]}),Object(k.jsxs)("a",{target:"_blank",href:"https://github.com/aimhubio/aim",rel:"noreferrer",className:"ExploreAim__social__item",onClick:function(){return Object(O.b)(o.a.home.createGithubIssue)},children:[Object(k.jsx)("img",{src:w,alt:"github"}),Object(k.jsxs)(C.n,{component:"span",tint:100,size:16,weight:400,children:["Create an issue ",Object(k.jsx)("br",{})," or report a bug to help us improve"]}),Object(k.jsx)(C.f,{name:"arrow-right"})]})]})]}),Object(k.jsxs)("div",{className:"ExploreAim__block__item",children:[Object(k.jsx)(C.n,{component:"h2",tint:100,weight:600,size:24,children:"Explore Aim"}),Object(k.jsx)("div",{className:"ExploreAim__card__container",children:z.map((function(e){return Object(k.jsx)(D,Object(l.a)({},e),e.path)}))})]})]})})}var M=c.a.memo(A),H=n(728),G=n(156);n(940);function I(e){e.askEmailSent,e.onSendEmail;return Object(k.jsx)(s.a,{children:Object(k.jsxs)("div",{className:"SetupGuide__container",children:[Object(k.jsx)(C.n,{component:"h2",size:24,weight:600,tint:100,children:"Integrate Aim with your code"}),Object(k.jsxs)("div",{className:"SetupGuide__code",children:[Object(k.jsx)(C.n,{component:"h3",size:18,tint:100,weight:600,children:"1. Import Aim"}),Object(k.jsx)(H.a,{code:"import aim"})]}),Object(k.jsxs)("div",{className:"SetupGuide__code",children:[Object(k.jsx)(C.n,{component:"h3",size:18,tint:100,weight:600,children:"2. Track your training runs"}),Object(k.jsx)(H.a,{code:"run_inst = aim.Run(experiment='my_exp_name')\n\n# Save inputs, hparams or any other `key: value` pairs\nrun_inst['hparams'] = {\n    'learning_rate': 0.01,\n    'batch_size': 32,\n}\n\n# Track metrics\nfor i in range(10):\n    run_inst.track(i, name='metric_name')"})]}),Object(k.jsxs)("div",{className:"SetupGuide__resources__container",children:[Object(k.jsxs)("a",{target:"_blank",href:G.b.STABLE,rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(O.b)(o.a.home.docs)},children:[Object(k.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(k.jsx)(C.f,{className:"SetupGuide__resources__item__icon_fullDocs",name:"full-docs"})}),Object(k.jsx)(C.n,{component:"span",size:14,tint:100,weight:500,children:"Documentation"})]}),Object(k.jsx)("div",{className:"SetupGuide__resources__item",children:Object(k.jsxs)("a",{target:"_blank",href:G.c.SETUP.COLAB_EXAMPLE,rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(O.b)(o.a.home.colab)},children:[Object(k.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(k.jsx)(C.f,{className:"SetupGuide__resources__item__icon_co",name:"co"})}),Object(k.jsx)(C.n,{component:"span",size:14,tint:100,weight:500,children:"Colab notebook"})]})}),Object(k.jsx)("div",{className:"SetupGuide__resources__item",children:Object(k.jsxs)("a",{target:"_blank",href:G.a.MAIN,rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(O.b)(o.a.home.liveDemo)},children:[Object(k.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(k.jsx)(C.f,{className:"SetupGuide__resources__item__icon_liveDemo",name:"live-demo"})}),Object(k.jsx)(C.n,{component:"span",size:14,tint:100,weight:500,children:"Live demo"})]})})]})]})})}var T=c.a.memo(I),W=n(717),B=n(569),R=n(6),F=n(67),J=n.n(F),P=n(85),L=n(336),Y=n(77),q=n(24),V=(n(941),[0,1,2,3,4]);var U=function(e){var t=e.data,n=e.startDate,a=e.endDate,i=e.cellSize,c=void 0===i?12:i,r=e.cellSpacing,l=void 0===r?4:r,d=e.scaleRange,m=void 0===d?4:d,u=e.onCellClick,j=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],p=Object(P.h)();n=new Date(n.getFullYear(),n.getMonth(),n.getDate()),a=new Date(a.getFullYear(),a.getMonth(),a.getDate());for(var x=n;0!==x.getDay();)x=y(x,-1);for(var h=a;0!==h.getDay();)h=y(h,1);0===h.getDay()&&(h=y(h,7));var _=Math.floor(Math.abs((x-h)/864e5)),b=Math.max.apply(Math,Object(R.a)(null===t||void 0===t?void 0:t.map((function(e){return null===e||void 0===e?void 0:e[1]})).filter((function(e){return Number.isInteger(e)})))),f=[].concat(Object(R.a)(j.slice(x.getMonth())),Object(R.a)(j.slice(0,x.getMonth()))),v={width:"".concat(_/7*c+(_/7-1)*l-50,"px")},g={gridTemplateColumns:"repeat(".concat(_/7,", 1fr)"),gridTemplateRows:"repeat(7, 1fr)",width:"".concat(_/7*c+(_/7-1)*l,"px"),height:"".concat(7*c+6*l,"px"),gridColumnGap:"".concat(l,"px"),gridRowGap:"".concat(l,"px")};function y(e,t){var n=new Date(e);return n.setDate(n.getDate()+t),n}function w(e){var t=Math.floor(e/7);return y(x,7*t+e%7)}function N(e){var n,i=function(e){for(var n=w(e),a=null,i=0;i<t.length;i++){var c,r,s;if((null===(c=t[i])||void 0===c?void 0:c[0].getFullYear())===n.getFullYear()&&(null===(r=t[i])||void 0===r?void 0:r[0].getMonth())===n.getMonth()&&(null===(s=t[i])||void 0===s?void 0:s[0].getDate())===n.getDate()){a=t[i];break}}return a}(e),c=w(e),r=i&&Number.isInteger(null===i||void 0===i?void 0:i[1])?(n=i[1],Math.ceil(n/b*m)):0,l=" ".concat(i?i[1]:0," tracked run").concat(1!==(null===i||void 0===i?void 0:i[1])?"s":""," on ").concat(j[c.getMonth()]," ").concat(c.getDate(),", ").concat(c.getFullYear());return Object(k.jsx)(s.a,{children:Object(k.jsx)("div",{className:"CalendarHeatmap__cell__wrapper",children:+a<+w(e)?Object(k.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--dummy"}):Object(k.jsx)(L.a,{title:l,children:Object(k.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(r),onClick:function(e){if(e.stopPropagation(),u(),r){var t=c.getTime(),n=Object(q.c)({query:"datetime(".concat(J()(t).format(Y.d),") <= run.created_at < datetime(").concat(J()(t).add(1,"day").format(Y.d),")")});O.b(o.a.home.activityCellClick),p.push("/runs?select=".concat(n))}},role:"navigation"})})})},e)}return Object(k.jsxs)("div",{className:"CalendarHeatmap",children:[Object(k.jsxs)("div",{className:"CalendarHeatmap__map",children:[Object(k.jsx)("div",{}),Object(k.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--x",style:v,children:f.slice(0,10).map((function(e,t){return Object(k.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--x",children:e},t)}))}),Object(k.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--y",children:["S","M","T","W","T","F","S"].map((function(e,t){return Object(k.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--y",children:e},t)}))}),Object(k.jsx)("div",{className:"CalendarHeatmap__map__grid",style:g,children:Object(R.a)(Array(_).keys()).map((function(e){return N(e)}))})]}),Object(k.jsxs)("div",{className:"CalendarHeatmap__cell__info",children:[Object(k.jsx)(C.n,{weight:400,size:12,children:"Less"}),V.map((function(e){return Object(k.jsx)("div",{style:{width:c,height:c},className:"CalendarHeatmap__cell__wrapper",children:Object(k.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(e)})},e)})),Object(k.jsx)(C.n,{weight:400,size:12,children:"More"})]})]})};n(942);function X(e){var t,n,a,i=e.activityData;var c=new Date;return Object(k.jsx)(s.a,{children:Object(k.jsxs)(W.a,{className:"Activity",container:!0,spacing:1,children:[Object(k.jsxs)(W.a,{item:!0,children:[Object(k.jsx)(C.n,{component:"h2",size:24,weight:600,tint:100,children:"Statistics"}),Object(k.jsxs)("div",{className:"Activity__Statistics__card",children:[Object(k.jsx)(C.n,{size:16,component:"span",color:"secondary",children:"Experiments"}),Object(k.jsx)(C.n,{component:"strong",size:36,weight:600,color:"secondary",children:null!==(t=null===i||void 0===i?void 0:i.num_experiments)&&void 0!==t?t:Object(k.jsx)(B.a,{className:"Activity__loader"})})]}),Object(k.jsxs)("div",{className:"Activity__Statistics__card",children:[Object(k.jsx)(C.n,{size:16,component:"span",color:"secondary",children:"Runs"}),Object(k.jsx)(C.n,{component:"strong",size:36,weight:600,color:"secondary",children:null!==(n=null===i||void 0===i?void 0:i.num_runs)&&void 0!==n?n:Object(k.jsx)(B.a,{className:"Activity__loader"})})]})]}),Object(k.jsxs)(W.a,{xs:!0,item:!0,children:[Object(k.jsx)(C.n,{component:"h2",size:24,weight:600,tint:100,children:"Activity"}),Object(k.jsx)("div",{className:"Activity__HeatMap",children:Object(k.jsx)(U,{startDate:function(e,t){var n=new Date(e);return n.setDate(n.getDate()+t),n}(c,-300),endDate:c,onCellClick:function(){Object(O.b)(o.a.home.activityCellClick)},data:Object.keys(null!==(a=null===i||void 0===i?void 0:i.activity_map)&&void 0!==a?a:{}).map((function(e){return[new Date(e),i.activity_map[e]]}))})})]})]})})}var $=c.a.memo(X);n(943);var K=function(e){var t=e.activityData,n=e.onSendEmail,a=e.notifyData,i=e.onNotificationDelete,c=e.askEmailSent;return Object(k.jsx)(s.a,{children:Object(k.jsxs)("section",{className:"Home__container",children:[Object(k.jsx)("div",{className:"Home__Activity__container",children:Object(k.jsx)($,{activityData:t})}),Object(k.jsxs)("div",{className:"Home__Explore__container",children:[Object(k.jsx)(T,{askEmailSent:c,onSendEmail:n}),Object(k.jsx)(M,{})]}),(null===a||void 0===a?void 0:a.length)>0&&Object(k.jsx)(y.a,{handleClose:i,data:a})]})})};t.default=function(){var e=Object(r.b)(g);return c.a.useEffect((function(){return g.initialize(),O.b(o.a.home.pageView),function(){g.destroy()}}),[]),Object(k.jsx)(s.a,{children:Object(k.jsx)(K,{onSendEmail:g.onSendEmail,activityData:e.activityData,notifyData:e.notifyData,askEmailSent:e.askEmailSent,onNotificationDelete:g.onHomeNotificationDelete})})}},658:function(e,t,n){"use strict";n.d(t,"a",(function(){return d}));n(0);var a=n(1433),i=n(1437),c=n(647),r=n.p+"static/media/successIcon.bd3fad23.svg",s=n.p+"static/media/errorIcon.09cae82c.svg",o=n(11),l=(n(659),n(1));function d(e){var t=e.data,n=void 0===t?[]:t,d=e.handleClose;return Object(l.jsx)(o.a,{children:Object(l.jsx)("div",{children:Object(l.jsx)(i.a,{open:!0,autoHideDuration:3e3,anchorOrigin:{vertical:"top",horizontal:"right"},children:Object(l.jsx)("div",{className:"NotificationContainer",children:n.map((function(e){var t=e.id,n=e.severity,i=e.messages;return Object(l.jsx)(c.a,{mt:.5,children:Object(l.jsx)(a.a,{onClose:function(){return d(+t)},variant:"outlined",severity:n,iconMapping:{success:Object(l.jsx)("img",{src:r,alt:""}),error:Object(l.jsx)("img",{src:s,alt:""})},style:{height:"auto"},children:Object(l.jsxs)("div",{className:"NotificationContainer__contentBox",children:[Object(l.jsx)("p",{className:"NotificationContainer__contentBox__severity",children:n}),i.map((function(e,t){return e?Object(l.jsx)("p",{className:"NotificationContainer__contentBox__message",children:e},t):null}))]})})},t)}))})})})})}},659:function(e,t,n){},717:function(e,t,n){"use strict";var a=n(9),i=n(3),c=n(0),r=(n(8),n(12)),s=n(19),o=[0,1,2,3,4,5,6,7,8,9,10],l=["auto",!0,1,2,3,4,5,6,7,8,9,10,11,12];function d(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:1,n=parseFloat(e);return"".concat(n/t).concat(String(e).replace(String(n),"")||"px")}var m=c.forwardRef((function(e,t){var n=e.alignContent,s=void 0===n?"stretch":n,o=e.alignItems,l=void 0===o?"stretch":o,d=e.classes,m=e.className,u=e.component,j=void 0===u?"div":u,p=e.container,x=void 0!==p&&p,h=e.direction,_=void 0===h?"row":h,b=e.item,f=void 0!==b&&b,v=e.justify,g=e.justifyContent,O=void 0===g?"flex-start":g,y=e.lg,w=void 0!==y&&y,N=e.md,C=void 0!==N&&N,S=e.sm,k=void 0!==S&&S,E=e.spacing,D=void 0===E?0:E,z=e.wrap,A=void 0===z?"wrap":z,M=e.xl,H=void 0!==M&&M,G=e.xs,I=void 0!==G&&G,T=e.zeroMinWidth,W=void 0!==T&&T,B=Object(a.a)(e,["alignContent","alignItems","classes","className","component","container","direction","item","justify","justifyContent","lg","md","sm","spacing","wrap","xl","xs","zeroMinWidth"]),R=Object(r.a)(d.root,m,x&&[d.container,0!==D&&d["spacing-xs-".concat(String(D))]],f&&d.item,W&&d.zeroMinWidth,"row"!==_&&d["direction-xs-".concat(String(_))],"wrap"!==A&&d["wrap-xs-".concat(String(A))],"stretch"!==l&&d["align-items-xs-".concat(String(l))],"stretch"!==s&&d["align-content-xs-".concat(String(s))],"flex-start"!==(v||O)&&d["justify-content-xs-".concat(String(v||O))],!1!==I&&d["grid-xs-".concat(String(I))],!1!==k&&d["grid-sm-".concat(String(k))],!1!==C&&d["grid-md-".concat(String(C))],!1!==w&&d["grid-lg-".concat(String(w))],!1!==H&&d["grid-xl-".concat(String(H))]);return c.createElement(j,Object(i.a)({className:R,ref:t},B))})),u=Object(s.a)((function(e){return Object(i.a)({root:{},container:{boxSizing:"border-box",display:"flex",flexWrap:"wrap",width:"100%"},item:{boxSizing:"border-box",margin:"0"},zeroMinWidth:{minWidth:0},"direction-xs-column":{flexDirection:"column"},"direction-xs-column-reverse":{flexDirection:"column-reverse"},"direction-xs-row-reverse":{flexDirection:"row-reverse"},"wrap-xs-nowrap":{flexWrap:"nowrap"},"wrap-xs-wrap-reverse":{flexWrap:"wrap-reverse"},"align-items-xs-center":{alignItems:"center"},"align-items-xs-flex-start":{alignItems:"flex-start"},"align-items-xs-flex-end":{alignItems:"flex-end"},"align-items-xs-baseline":{alignItems:"baseline"},"align-content-xs-center":{alignContent:"center"},"align-content-xs-flex-start":{alignContent:"flex-start"},"align-content-xs-flex-end":{alignContent:"flex-end"},"align-content-xs-space-between":{alignContent:"space-between"},"align-content-xs-space-around":{alignContent:"space-around"},"justify-content-xs-center":{justifyContent:"center"},"justify-content-xs-flex-end":{justifyContent:"flex-end"},"justify-content-xs-space-between":{justifyContent:"space-between"},"justify-content-xs-space-around":{justifyContent:"space-around"},"justify-content-xs-space-evenly":{justifyContent:"space-evenly"}},function(e,t){var n={};return o.forEach((function(a){var i=e.spacing(a);0!==i&&(n["spacing-".concat(t,"-").concat(a)]={margin:"-".concat(d(i,2)),width:"calc(100% + ".concat(d(i),")"),"& > $item":{padding:d(i,2)}})})),n}(e,"xs"),e.breakpoints.keys.reduce((function(t,n){return function(e,t,n){var a={};l.forEach((function(e){var t="grid-".concat(n,"-").concat(e);if(!0!==e)if("auto"!==e){var i="".concat(Math.round(e/12*1e8)/1e6,"%");a[t]={flexBasis:i,flexGrow:0,maxWidth:i}}else a[t]={flexBasis:"auto",flexGrow:0,maxWidth:"none"};else a[t]={flexBasis:0,flexGrow:1,maxWidth:"100%"}})),"xs"===n?Object(i.a)(e,a):e[t.breakpoints.up(n)]=a}(t,e,n),t}),{}))}),{name:"MuiGrid"})(m);t.a=u},728:function(e,t,n){"use strict";var a=n(2),i=n(0),c=n.n(i),r=n(340),s=n(348),o=n(11),l=n(199),d=(n(729),n(1));function m(e){var t=e.code,n=void 0===t?"":t,i=e.className,m=void 0===i?"":i,u=e.language,j=void 0===u?"python":u,p=Object(r.c)(),x=c.a.useRef(null),h=c.a.useMemo((function(){return Object(l.a)()}),[]);return c.a.useEffect((function(){h.theme.config.colors=Object(a.a)(Object(a.a)({},h.theme.config.colors),{},{"editor.background":"#f2f3f4"}),p&&x.current&&(p.editor.colorizeElement(x.current,{theme:j}),p.editor.defineTheme(h.theme.name,h.theme.config),p.editor.setTheme(h.theme.name))}),[p]),Object(d.jsx)(o.a,{children:Object(d.jsxs)("div",{className:"CodeBlock ".concat(m," "),children:[Object(d.jsx)("pre",{className:"ScrollBar__hidden","data-lang":j,ref:x,children:n}),Object(d.jsx)(o.a,{children:Object(d.jsx)(s.a,{className:"CodeBlock__copy__button",contentRef:x})})]})})}t.a=c.a.memo(m)},729:function(e,t,n){},938:function(e,t,n){},939:function(e,t,n){},940:function(e,t,n){},941:function(e,t,n){},942:function(e,t,n){},943:function(e,t,n){}}]);
//# sourceMappingURL=home.js.map?version=30f959946b3313885600