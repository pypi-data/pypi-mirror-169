(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[13],{1534:function(e,t,r){"use strict";var n,o=r(0),i=r.n(o),a=r(19),c="small",u="medium",l="large",s=r(30),f=r(89);function d(){return(d=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function p(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function y(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?p(Object(r),!0).forEach((function(t){g(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):p(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function g(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function b(e){var t;return(t={},g(t,c,"2px"),g(t,u,"4px"),g(t,l,"8px"),t)[e]}var m=Object(s.a)("div",(function(e){return{width:"100%"}}));m.displayName="StyledRoot",m.displayName="StyledRoot";var v=Object(s.a)("div",(function(e){var t=e.$theme.sizing;return{display:"flex",marginLeft:t.scale500,marginRight:t.scale500,marginTop:t.scale500,marginBottom:t.scale500}}));v.displayName="StyledBarContainer",v.displayName="StyledBarContainer";var h=Object(s.a)("div",(function(e){var t=e.$theme,r=e.$size,n=e.$steps,o=t.colors,i=t.sizing,a=t.borders.useRoundedCorners?i.scale0:0;return y({borderTopLeftRadius:a,borderTopRightRadius:a,borderBottomRightRadius:a,borderBottomLeftRadius:a,backgroundColor:Object(f.b)(o.progressbarTrackFill,"0.16"),height:b(r),flex:1,overflow:"hidden"},n<2?{}:{marginLeft:i.scale300,":first-child":{marginLeft:"0"}})}));h.displayName="StyledBar",h.displayName="StyledBar";var w=Object(s.a)("div",(function(e){var t=e.$theme,r=e.$value,n=e.$successValue,o=e.$steps,i=e.$index,a=e.$maxValue,c=e.$minValue,u=void 0===c?0:c,l=a||n,s=t.colors,f=t.sizing,d=t.borders,p="".concat(100-100*(r-u)/(l-u),"%"),g="awaits",b="inProgress",m="completed",v="default";if(o>1){var h=(l-u)/o,w=(r-u)/(l-u)*100,O=Math.floor(w/h);v=i<O?m:i===O?b:g}var j=d.useRoundedCorners?f.scale0:0,D={transform:"translateX(-".concat(p,")")},P=v===b?{animationDuration:"2.1s",animationIterationCount:"infinite",animationTimingFunction:t.animation.linearCurve,animationName:{"0%":{transform:"translateX(-102%)",opacity:1},"50%":{transform:"translateX(0%)",opacity:1},"100%":{transform:"translateX(0%)",opacity:0}}}:v===m?{transform:"translateX(0%)"}:{transform:"translateX(-102%)"};return y({borderTopLeftRadius:j,borderTopRightRadius:j,borderBottomRightRadius:j,borderBottomLeftRadius:j,backgroundColor:s.accent,height:"100%",width:"100%",transform:"translateX(-102%)",transition:"transform 0.5s"},o>1?P:D)}));w.displayName="StyledBarProgress",w.displayName="StyledBarProgress";var O=Object(s.a)("div",(function(e){var t=e.$theme,r=e.$isLeft,n=void 0!==r&&r,o=e.$size,i=void 0===o?u:o,a=t.colors,c=t.sizing,l=t.borders.useRoundedCorners?c.scale0:0,s=b(i),f={display:"inline-block",flex:1,marginLeft:"auto",marginRight:"auto",transitionProperty:"background-position",animationDuration:"1.5s",animationIterationCount:"infinite",animationTimingFunction:t.animation.linearCurve,backgroundSize:"300% auto",backgroundRepeat:"no-repeat",backgroundPositionX:n?"-50%":"150%",backgroundImage:"linear-gradient(".concat(n?"90":"270","deg, transparent 0%, ").concat(a.accent," 25%, ").concat(a.accent," 75%, transparent 100%)"),animationName:n?{"0%":{backgroundPositionX:"-50%"},"33%":{backgroundPositionX:"50%"},"66%":{backgroundPositionX:"50%"},"100%":{backgroundPositionX:"150%"}}:{"0%":{backgroundPositionX:"150%"},"33%":{backgroundPositionX:"50%"},"66%":{backgroundPositionX:"50%"},"100%":{backgroundPositionX:"-50%"}}};return y(y({},n?{borderTopLeftRadius:l,borderBottomLeftRadius:l}:{borderTopRightRadius:l,borderBottomRightRadius:l}),{},{height:s},f)}));O.displayName="StyledInfiniteBar",O.displayName="StyledInfiniteBar";var j=Object(s.a)("div",(function(e){return y(y({textAlign:"center"},e.$theme.typography.font150),{},{color:e.$theme.colors.contentTertiary})}));j.displayName="StyledLabel",j.displayName="StyledLabel";var D=(g(n={},l,{d:"M47.5 4H71.5529C82.2933 4 91 12.9543 91 24C91 35.0457 82.2933 44 71.5529 44H23.4471C12.7067 44 4 35.0457 4 24C4 12.9543 12.7067 4 23.4471 4H47.5195",width:95,height:48,strokeWidth:8,typography:"LabelLarge"}),g(n,u,{d:"M39 2H60.5833C69.0977 2 76 9.16344 76 18C76 26.8366 69.0977 34 60.5833 34H17.4167C8.90228 34 2 26.8366 2 18C2 9.16344 8.90228 2 17.4167 2H39.0195",width:78,height:36,strokeWidth:4,typography:"LabelMedium"}),g(n,c,{d:"M32 1H51.6271C57.9082 1 63 6.37258 63 13C63 19.6274 57.9082 25 51.6271 25H12.3729C6.09181 25 1 19.6274 1 13C1 6.37258 6.09181 1 12.3729 1H32.0195",width:64,height:26,strokeWidth:2,typography:"LabelSmall"}),n),P=Object(s.a)("div",(function(e){var t=e.$size,r=e.$inline;return{width:D[t].width+"px",height:D[t].height+"px",position:"relative",display:r?"inline-flex":"flex",alignItems:"center",justifyContent:"center"}}));P.displayName="StyledProgressBarRoundedRoot",P.displayName="StyledProgressBarRoundedRoot";var S=Object(s.a)("svg",(function(e){var t=e.$size;return{width:D[t].width+"px",height:D[t].height+"px",position:"absolute",fill:"none"}}));S.displayName="_StyledProgressBarRoundedSvg",S.displayName="_StyledProgressBarRoundedSvg";Object(s.d)(S,(function(e){return function(t){return i.a.createElement(e,d({viewBox:"0 0 ".concat(D[t.$size].width," ").concat(D[t.$size].height),xmlns:"http://www.w3.org/2000/svg"},t))}}));var k=Object(s.a)("path",(function(e){var t=e.$theme,r=e.$size;return{stroke:t.colors.backgroundTertiary,strokeWidth:D[r].strokeWidth+"px"}}));k.displayName="_StyledProgressBarRoundedTrackBackground",k.displayName="_StyledProgressBarRoundedTrackBackground";Object(s.d)(k,(function(e){return function(t){return i.a.createElement(e,d({d:D[t.$size].d},t))}}));var x=Object(s.a)("path",(function(e){var t=e.$theme,r=e.$size,n=e.$visible,o=e.$pathLength,i=e.$pathProgress;return{visibility:n?"visible":"hidden",stroke:t.colors.borderAccent,strokeWidth:D[r].strokeWidth+"px",strokeDasharray:o,strokeDashoffset:o*(1-i)+""}}));x.displayName="_StyledProgressBarRoundedTrackForeground",x.displayName="_StyledProgressBarRoundedTrackForeground";Object(s.d)(x,(function(e){return function(t){return i.a.createElement(e,d({d:D[t.$size].d},t))}}));var R=Object(s.a)("div",(function(e){var t=e.$theme,r=e.$size;return y({color:t.colors.contentPrimary},t.typography[D[r].typography])}));function C(e){return(C="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}R.displayName="StyledProgressBarRoundedText",R.displayName="StyledProgressBarRoundedText";var E=["overrides","getProgressLabel","value","size","steps","successValue","minValue","maxValue","showLabel","infinite","errorMessage","forwardedRef"];function A(){return(A=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function z(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!==typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,o,i=[],a=!0,c=!1;try{for(r=r.call(e);!(a=(n=r.next()).done)&&(i.push(n.value),!t||i.length!==t);a=!0);}catch(u){c=!0,o=u}finally{try{a||null==r.return||r.return()}finally{if(c)throw o}}return i}(e,t)||function(e,t){if(!e)return;if("string"===typeof e)return F(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return F(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function F(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function $(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}function B(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function L(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function T(e,t){return(T=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,t){return e.__proto__=t,e})(e,t)}function N(e){var t=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,n=M(e);if(t){var o=M(this).constructor;r=Reflect.construct(n,arguments,o)}else r=n.apply(this,arguments);return V(this,r)}}function V(e,t){if(t&&("object"===C(t)||"function"===typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e)}function M(e){return(M=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}var I,H,_,X=function(e){!function(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),Object.defineProperty(e,"prototype",{writable:!1}),t&&T(e,t)}(c,e);var t,r,n,i=N(c);function c(){return B(this,c),i.apply(this,arguments)}return t=c,(r=[{key:"componentDidMount",value:function(){}},{key:"render",value:function(){var e=this.props,t=e.overrides,r=void 0===t?{}:t,n=e.getProgressLabel,i=e.value,c=e.size,u=e.steps,l=e.successValue,s=e.minValue,f=e.maxValue,d=e.showLabel,p=e.infinite,y=e.errorMessage,g=e.forwardedRef,b=$(e,E),D=this.props["aria-label"]||this.props.ariaLabel,P=100!==f?f:l,S=z(Object(a.c)(r.Root,m),2),k=S[0],x=S[1],R=z(Object(a.c)(r.BarContainer,v),2),C=R[0],F=R[1],B=z(Object(a.c)(r.Bar,h),2),L=B[0],T=B[1],N=z(Object(a.c)(r.BarProgress,w),2),V=N[0],M=N[1],I=z(Object(a.c)(r.Label,j),2),H=I[0],_=I[1],X=z(Object(a.c)(r.InfiniteBar,O),2),K=X[0],W=X[1],U={$infinite:p,$size:c,$steps:u,$successValue:P,$minValue:s,$maxValue:P,$value:i};return o.createElement(k,A({ref:g,"data-baseweb":"progress-bar",role:"progressbar","aria-label":D||n(i,P,s),"aria-valuenow":p?null:i,"aria-valuemin":p?null:s,"aria-valuemax":p?null:P,"aria-invalid":!!y||null,"aria-errormessage":y},b,U,x),o.createElement(C,A({},U,F),p?o.createElement(o.Fragment,null,o.createElement(K,A({$isLeft:!0,$size:U.$size},W)),o.createElement(K,A({$size:U.$size},W))):function(){for(var e=[],t=0;t<u;t++)e.push(o.createElement(L,A({key:t},U,T),o.createElement(V,A({$index:t},U,M))));return e}()),d&&o.createElement(H,A({},U,_),n(i,P,s)))}}])&&L(t.prototype,r),n&&L(t,n),Object.defineProperty(t,"prototype",{writable:!1}),c}(o.Component);_={getProgressLabel:function(e,t,r){return"".concat(Math.round((e-r)/(t-r)*100),"% Loaded")},infinite:!1,overrides:{},showLabel:!1,size:u,steps:1,successValue:100,minValue:0,maxValue:100,value:0},(H="defaultProps")in(I=X)?Object.defineProperty(I,H,{value:_,enumerable:!0,configurable:!0,writable:!0}):I[H]=_;var K=o.forwardRef((function(e,t){return o.createElement(X,A({forwardedRef:t},e))}));K.displayName="ProgressBar";t.a=K},1723:function(e,t,r){"use strict";t.__esModule=!0,t.default=function(e,t){if(e&&t){var r=Array.isArray(t)?t:t.split(","),n=e.name||"",o=(e.type||"").toLowerCase(),i=o.replace(/\/.*$/,"");return r.some((function(e){var t=e.trim().toLowerCase();return"."===t.charAt(0)?n.toLowerCase().endsWith(t):t.endsWith("/*")?i===t.replace(/\/.*$/,""):o===t}))}return!0}},1732:function(e,t,r){"use strict";var n=r(0),o=r.n(n),i=r(13),a=r.n(i);function c(e,t,r,n){return new(r||(r=Promise))((function(o,i){function a(e){try{u(n.next(e))}catch(t){i(t)}}function c(e){try{u(n.throw(e))}catch(t){i(t)}}function u(e){var t;e.done?o(e.value):(t=e.value,t instanceof r?t:new r((function(e){e(t)}))).then(a,c)}u((n=n.apply(e,t||[])).next())}))}function u(e,t){var r,n,o,i,a={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return i={next:c(0),throw:c(1),return:c(2)},"function"===typeof Symbol&&(i[Symbol.iterator]=function(){return this}),i;function c(i){return function(c){return function(i){if(r)throw new TypeError("Generator is already executing.");for(;a;)try{if(r=1,n&&(o=2&i[0]?n.return:i[0]?n.throw||((o=n.return)&&o.call(n),0):n.next)&&!(o=o.call(n,i[1])).done)return o;switch(n=0,o&&(i=[2&i[0],o.value]),i[0]){case 0:case 1:o=i;break;case 4:return a.label++,{value:i[1],done:!1};case 5:a.label++,n=i[1],i=[0];continue;case 7:i=a.ops.pop(),a.trys.pop();continue;default:if(!(o=(o=a.trys).length>0&&o[o.length-1])&&(6===i[0]||2===i[0])){a=0;continue}if(3===i[0]&&(!o||i[1]>o[0]&&i[1]<o[3])){a.label=i[1];break}if(6===i[0]&&a.label<o[1]){a.label=o[1],o=i;break}if(o&&a.label<o[2]){a.label=o[2],a.ops.push(i);break}o[2]&&a.ops.pop(),a.trys.pop();continue}i=t.call(e,a)}catch(c){i=[6,c],n=0}finally{r=o=0}if(5&i[0])throw i[1];return{value:i[0]?i[1]:void 0,done:!0}}([i,c])}}}Object.create;function l(e,t){var r="function"===typeof Symbol&&e[Symbol.iterator];if(!r)return e;var n,o,i=r.call(e),a=[];try{for(;(void 0===t||t-- >0)&&!(n=i.next()).done;)a.push(n.value)}catch(c){o={error:c}}finally{try{n&&!n.done&&(r=i.return)&&r.call(i)}finally{if(o)throw o.error}}return a}Object.create;var s=new Map([["avi","video/avi"],["gif","image/gif"],["ico","image/x-icon"],["jpeg","image/jpeg"],["jpg","image/jpeg"],["mkv","video/x-matroska"],["mov","video/quicktime"],["mp4","video/mp4"],["pdf","application/pdf"],["png","image/png"],["zip","application/zip"],["doc","application/msword"],["docx","application/vnd.openxmlformats-officedocument.wordprocessingml.document"]]);function f(e,t){var r=function(e){var t=e.name;if(t&&-1!==t.lastIndexOf(".")&&!e.type){var r=t.split(".").pop().toLowerCase(),n=s.get(r);n&&Object.defineProperty(e,"type",{value:n,writable:!1,configurable:!1,enumerable:!0})}return e}(e);if("string"!==typeof r.path){var n=e.webkitRelativePath;Object.defineProperty(r,"path",{value:"string"===typeof t?t:"string"===typeof n&&n.length>0?n:e.name,writable:!1,configurable:!1,enumerable:!0})}return r}var d=[".DS_Store","Thumbs.db"];function p(e){return(null!==e.target&&e.target.files?b(e.target.files):[]).map((function(e){return f(e)}))}function y(e,t){return c(this,void 0,void 0,(function(){var r;return u(this,(function(n){switch(n.label){case 0:return e.items?(r=b(e.items).filter((function(e){return"file"===e.kind})),"drop"!==t?[2,r]:[4,Promise.all(r.map(m))]):[3,2];case 1:return[2,g(v(n.sent()))];case 2:return[2,g(b(e.files).map((function(e){return f(e)})))]}}))}))}function g(e){return e.filter((function(e){return-1===d.indexOf(e.name)}))}function b(e){for(var t=[],r=0;r<e.length;r++){var n=e[r];t.push(n)}return t}function m(e){if("function"!==typeof e.webkitGetAsEntry)return h(e);var t=e.webkitGetAsEntry();return t&&t.isDirectory?O(t):h(e)}function v(e){return e.reduce((function(e,t){return function(){for(var e=[],t=0;t<arguments.length;t++)e=e.concat(l(arguments[t]));return e}(e,Array.isArray(t)?v(t):[t])}),[])}function h(e){var t=e.getAsFile();if(!t)return Promise.reject(e+" is not a File");var r=f(t);return Promise.resolve(r)}function w(e){return c(this,void 0,void 0,(function(){return u(this,(function(t){return[2,e.isDirectory?O(e):j(e)]}))}))}function O(e){var t=e.createReader();return new Promise((function(e,r){var n=[];!function o(){var i=this;t.readEntries((function(t){return c(i,void 0,void 0,(function(){var i,a,c;return u(this,(function(u){switch(u.label){case 0:if(t.length)return[3,5];u.label=1;case 1:return u.trys.push([1,3,,4]),[4,Promise.all(n)];case 2:return i=u.sent(),e(i),[3,4];case 3:return a=u.sent(),r(a),[3,4];case 4:return[3,6];case 5:c=Promise.all(t.map(w)),n.push(c),o(),u.label=6;case 6:return[2]}}))}))}),(function(e){r(e)}))}()}))}function j(e){return c(this,void 0,void 0,(function(){return u(this,(function(t){return[2,new Promise((function(t,r){e.file((function(r){var n=f(r,e.fullPath);t(n)}),(function(e){r(e)}))}))]}))}))}var D=r(1723),P=r.n(D);function S(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if("undefined"===typeof Symbol||!(Symbol.iterator in Object(e)))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,c=e[Symbol.iterator]();!(n=(a=c.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(u){o=!0,i=u}finally{try{n||null==c.return||c.return()}finally{if(o)throw i}}return r}(e,t)||function(e,t){if(!e)return;if("string"===typeof e)return k(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return k(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}var x=function(e){e=Array.isArray(e)&&1===e.length?e[0]:e;var t=Array.isArray(e)?"one of ".concat(e.join(", ")):e;return{code:"file-invalid-type",message:"File type must be ".concat(t)}},R=function(e){return{code:"file-too-large",message:"File is larger than ".concat(e," bytes")}},C=function(e){return{code:"file-too-small",message:"File is smaller than ".concat(e," bytes")}},E={code:"too-many-files",message:"Too many files"};function A(e,t){var r="application/x-moz-file"===e.type||P()(e,t);return[r,r?null:x(t)]}function z(e,t,r){if(F(e.size))if(F(t)&&F(r)){if(e.size>r)return[!1,R(r)];if(e.size<t)return[!1,C(t)]}else{if(F(t)&&e.size<t)return[!1,C(t)];if(F(r)&&e.size>r)return[!1,R(r)]}return[!0,null]}function F(e){return void 0!==e&&null!==e}function $(e){var t=e.files,r=e.accept,n=e.minSize,o=e.maxSize,i=e.multiple,a=e.maxFiles;return!(!i&&t.length>1||i&&a>=1&&t.length>a)&&t.every((function(e){var t=S(A(e,r),1)[0],i=S(z(e,n,o),1)[0];return t&&i}))}function B(e){return"function"===typeof e.isPropagationStopped?e.isPropagationStopped():"undefined"!==typeof e.cancelBubble&&e.cancelBubble}function L(e){return e.dataTransfer?Array.prototype.some.call(e.dataTransfer.types,(function(e){return"Files"===e||"application/x-moz-file"===e})):!!e.target&&!!e.target.files}function T(e){e.preventDefault()}function N(e){return-1!==e.indexOf("MSIE")||-1!==e.indexOf("Trident/")}function V(e){return-1!==e.indexOf("Edge/")}function M(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:window.navigator.userAgent;return N(e)||V(e)}function I(){for(var e=arguments.length,t=new Array(e),r=0;r<e;r++)t[r]=arguments[r];return function(e){for(var r=arguments.length,n=new Array(r>1?r-1:0),o=1;o<r;o++)n[o-1]=arguments[o];return t.some((function(t){return!B(e)&&t&&t.apply(void 0,[e].concat(n)),B(e)}))}}function H(e){return function(e){if(Array.isArray(e))return K(e)}(e)||function(e){if("undefined"!==typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(e)||X(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function _(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if("undefined"===typeof Symbol||!(Symbol.iterator in Object(e)))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,c=e[Symbol.iterator]();!(n=(a=c.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(u){o=!0,i=u}finally{try{n||null==c.return||c.return()}finally{if(o)throw i}}return r}(e,t)||X(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function X(e,t){if(e){if("string"===typeof e)return K(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?K(e,t):void 0}}function K(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function W(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function U(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?W(Object(r),!0).forEach((function(t){G(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):W(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function G(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function q(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var J=Object(n.forwardRef)((function(e,t){var r=e.children,i=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=U(U({},Q),e),r=t.accept,o=t.disabled,i=t.getFilesFromEvent,a=t.maxSize,c=t.minSize,u=t.multiple,l=t.maxFiles,s=t.onDragEnter,f=t.onDragLeave,d=t.onDragOver,p=t.onDrop,y=t.onDropAccepted,g=t.onDropRejected,b=t.onFileDialogCancel,m=t.preventDropOnDocument,v=t.noClick,h=t.noKeyboard,w=t.noDrag,O=t.noDragEventsBubbling,j=Object(n.useRef)(null),D=Object(n.useRef)(null),P=_(Object(n.useReducer)(Z,Y),2),S=P[0],k=P[1],x=S.isFocused,R=S.isFileDialogActive,C=S.draggedFiles,F=Object(n.useCallback)((function(){D.current&&(k({type:"openDialog"}),D.current.value=null,D.current.click())}),[k]),N=function(){R&&setTimeout((function(){D.current&&(D.current.files.length||(k({type:"closeDialog"}),"function"===typeof b&&b()))}),300)};Object(n.useEffect)((function(){return window.addEventListener("focus",N,!1),function(){window.removeEventListener("focus",N,!1)}}),[D,R,b]);var V=Object(n.useCallback)((function(e){j.current&&j.current.isEqualNode(e.target)&&(32!==e.keyCode&&13!==e.keyCode||(e.preventDefault(),F()))}),[j,D]),X=Object(n.useCallback)((function(){k({type:"focus"})}),[]),K=Object(n.useCallback)((function(){k({type:"blur"})}),[]),W=Object(n.useCallback)((function(){v||(M()?setTimeout(F,0):F())}),[D,v]),J=Object(n.useRef)([]),ee=function(e){j.current&&j.current.contains(e.target)||(e.preventDefault(),J.current=[])};Object(n.useEffect)((function(){return m&&(document.addEventListener("dragover",T,!1),document.addEventListener("drop",ee,!1)),function(){m&&(document.removeEventListener("dragover",T),document.removeEventListener("drop",ee))}}),[j,m]);var te=Object(n.useCallback)((function(e){e.preventDefault(),e.persist(),ue(e),J.current=[].concat(H(J.current),[e.target]),L(e)&&Promise.resolve(i(e)).then((function(t){B(e)&&!O||(k({draggedFiles:t,isDragActive:!0,type:"setDraggedFiles"}),s&&s(e))}))}),[i,s,O]),re=Object(n.useCallback)((function(e){if(e.preventDefault(),e.persist(),ue(e),e.dataTransfer)try{e.dataTransfer.dropEffect="copy"}catch(t){}return L(e)&&d&&d(e),!1}),[d,O]),ne=Object(n.useCallback)((function(e){e.preventDefault(),e.persist(),ue(e);var t=J.current.filter((function(e){return j.current&&j.current.contains(e)})),r=t.indexOf(e.target);-1!==r&&t.splice(r,1),J.current=t,t.length>0||(k({isDragActive:!1,type:"setDraggedFiles",draggedFiles:[]}),L(e)&&f&&f(e))}),[j,f,O]),oe=Object(n.useCallback)((function(e){e.preventDefault(),e.persist(),ue(e),J.current=[],L(e)&&Promise.resolve(i(e)).then((function(t){if(!B(e)||O){var n=[],o=[];t.forEach((function(e){var t=_(A(e,r),2),i=t[0],u=t[1],l=_(z(e,c,a),2),s=l[0],f=l[1];if(i&&s)n.push(e);else{var d=[u,f].filter((function(e){return e}));o.push({file:e,errors:d})}})),(!u&&n.length>1||u&&l>=1&&n.length>l)&&(n.forEach((function(e){o.push({file:e,errors:[E]})})),n.splice(0)),k({acceptedFiles:n,fileRejections:o,type:"setFiles"}),p&&p(n,o,e),o.length>0&&g&&g(o,e),n.length>0&&y&&y(n,e)}})),k({type:"reset"})}),[u,r,c,a,l,i,p,y,g,O]),ie=function(e){return o?null:e},ae=function(e){return h?null:ie(e)},ce=function(e){return w?null:ie(e)},ue=function(e){O&&e.stopPropagation()},le=Object(n.useMemo)((function(){return function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.refKey,r=void 0===t?"ref":t,n=e.onKeyDown,i=e.onFocus,a=e.onBlur,c=e.onClick,u=e.onDragEnter,l=e.onDragOver,s=e.onDragLeave,f=e.onDrop,d=q(e,["refKey","onKeyDown","onFocus","onBlur","onClick","onDragEnter","onDragOver","onDragLeave","onDrop"]);return U(U(G({onKeyDown:ae(I(n,V)),onFocus:ae(I(i,X)),onBlur:ae(I(a,K)),onClick:ie(I(c,W)),onDragEnter:ce(I(u,te)),onDragOver:ce(I(l,re)),onDragLeave:ce(I(s,ne)),onDrop:ce(I(f,oe))},r,j),o||h?{}:{tabIndex:0}),d)}}),[j,V,X,K,W,te,re,ne,oe,h,w,o]),se=Object(n.useCallback)((function(e){e.stopPropagation()}),[]),fe=Object(n.useMemo)((function(){return function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.refKey,n=void 0===t?"ref":t,o=e.onChange,i=e.onClick,a=q(e,["refKey","onChange","onClick"]);return U(U({},G({accept:r,multiple:u,type:"file",style:{display:"none"},onChange:ie(I(o,oe)),onClick:ie(I(i,se)),autoComplete:"off",tabIndex:-1},n,D)),a)}}),[D,r,u,oe,o]),de=C.length,pe=de>0&&$({files:C,accept:r,minSize:c,maxSize:a,multiple:u,maxFiles:l}),ye=de>0&&!pe;return U(U({},S),{},{isDragAccept:pe,isDragReject:ye,isFocused:x&&!o,getRootProps:le,getInputProps:fe,rootRef:j,inputRef:D,open:ie(F)})}(q(e,["children"])),a=i.open,c=q(i,["open"]);return Object(n.useImperativeHandle)(t,(function(){return{open:a}}),[a]),o.a.createElement(n.Fragment,null,r(U(U({},c),{},{open:a})))}));J.displayName="Dropzone";var Q={disabled:!1,getFilesFromEvent:function(e){return c(this,void 0,void 0,(function(){return u(this,(function(t){return[2,(r=e,r.dataTransfer&&e.dataTransfer?y(e.dataTransfer,e.type):p(e))];var r}))}))},maxSize:1/0,minSize:0,multiple:!0,maxFiles:0,preventDropOnDocument:!0,noClick:!1,noKeyboard:!1,noDrag:!1,noDragEventsBubbling:!1};J.defaultProps=Q,J.propTypes={children:a.a.func,accept:a.a.oneOfType([a.a.string,a.a.arrayOf(a.a.string)]),multiple:a.a.bool,preventDropOnDocument:a.a.bool,noClick:a.a.bool,noKeyboard:a.a.bool,noDrag:a.a.bool,noDragEventsBubbling:a.a.bool,minSize:a.a.number,maxSize:a.a.number,maxFiles:a.a.number,disabled:a.a.bool,getFilesFromEvent:a.a.func,onFileDialogCancel:a.a.func,onDragEnter:a.a.func,onDragLeave:a.a.func,onDragOver:a.a.func,onDrop:a.a.func,onDropAccepted:a.a.func,onDropRejected:a.a.func};t.a=J;var Y={isFocused:!1,isFileDialogActive:!1,isDragActive:!1,isDragAccept:!1,isDragReject:!1,draggedFiles:[],acceptedFiles:[],fileRejections:[]};function Z(e,t){switch(t.type){case"focus":return U(U({},e),{},{isFocused:!0});case"blur":return U(U({},e),{},{isFocused:!1});case"openDialog":return U(U({},e),{},{isFileDialogActive:!0});case"closeDialog":return U(U({},e),{},{isFileDialogActive:!1});case"setDraggedFiles":var r=t.isDragActive,n=t.draggedFiles;return U(U({},e),{},{draggedFiles:n,isDragActive:r});case"setFiles":return U(U({},e),{},{acceptedFiles:t.acceptedFiles,fileRejections:t.fileRejections});case"reset":return U(U({},e),{},{isFileDialogActive:!1,isDragActive:!1,draggedFiles:[],acceptedFiles:[],fileRejections:[]});default:return e}}},1798:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(71),o=r.n(n),i=r(0),a=r(47),c=i.forwardRef((function(e,t){return i.createElement(a.a,o()({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 24 24"},e,{ref:t}),i.createElement("path",{fill:"none",d:"M0 0h24v24H0V0z"}),i.createElement("path",{d:"M19.35 10.04A7.49 7.49 0 0012 4C9.11 4 6.6 5.64 5.35 8.04A5.994 5.994 0 000 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM19 18H6c-2.21 0-4-1.79-4-4 0-2.05 1.53-3.76 3.56-3.97l1.07-.11.5-.95A5.469 5.469 0 0112 6c2.62 0 4.88 1.86 5.39 4.43l.3 1.5 1.53.11A2.98 2.98 0 0122 15c0 1.65-1.35 3-3 3zM8 13h2.55v3h2.9v-3H16l-4-4z"}))}));c.displayName="CloudUpload"},1799:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(71),o=r.n(n),i=r(0),a=r(47),c=i.forwardRef((function(e,t){return i.createElement(a.a,o()({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 24 24"},e,{ref:t}),i.createElement("path",{fill:"none",d:"M0 0h24v24H0V0z"}),i.createElement("path",{d:"M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12l4.58-4.59z"}))}));c.displayName="ChevronLeft"},1800:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(71),o=r.n(n),i=r(0),a=r(47),c=i.forwardRef((function(e,t){return i.createElement(a.a,o()({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 24 24"},e,{ref:t}),i.createElement("path",{d:"M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"}))}));c.displayName="Error"},1801:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(71),o=r.n(n),i=r(0),a=r(47),c=i.forwardRef((function(e,t){return i.createElement(a.a,o()({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 24 24"},e,{ref:t}),i.createElement("path",{fill:"none",d:"M0 0h24v24H0V0z"}),i.createElement("path",{d:"M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zM6 20V4h7v5h5v11H6z"}))}));c.displayName="InsertDriveFile"},1802:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(71),o=r.n(n),i=r(0),a=r(47),c=i.forwardRef((function(e,t){return i.createElement(a.a,o()({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 24 24"},e,{ref:t}),i.createElement("path",{fill:"none",d:"M0 0h24v24H0V0z"}),i.createElement("path",{d:"M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"}))}));c.displayName="Clear"}}]);