// CREATED ON 8-15-16 :: N. ANTONOPULOS - DEV ::
// FF-FEED AD
//------------------------------------------
//STEP 1 : CHECK TO MAKE SURE IA VARS ARE LOADED
//STEP 2A : if useFeed is 'yes' load feed if no setup default
//STEP 2B : do not load feed.
//STEP 3 : Build ad elements l
//STEP 4 : load images including default or feed hero image
//STEP 5 : add event listeners
//STEP 6 : run ad
//------------------------------------------
//// GLOBAL VARS //////
var adW = 728;
var adH = 90;
var isDefault = false;
var feedReturned = false;
var imagesLoaded = false;
var cityNm;
var parser, xmlDoc;
var prodURL;
var productClicked;
var border = document.getElementById("banner-border");
        border.style.width = (adW-2) + "px";
        border.style.height = (adH-2) + "px";

var creative = {
    init: function () {
        myFT.on("instantads", function() {
            //check to see if set to default style is
            //A - load the correct css file
            // if style is default fire the feedLoadError function else try feed
            cityNm = (myFT.instantAds.default_city).toUpperCase();
            if(myFT.instantAds.useFeed.toLowerCase() === 'yes'){
                var feedEndpoint = myFT.instantAds.feedEndpoint;
                var destinationSegment = myFT.instantAds.segmentID;
                var destinationEnigma = myFT.get('ftDestinationEnigma') || '';
                if(destinationEnigma == ''){

                    if(creative.checkSegmentInParam(destinationSegment)){
                        destinationEnigma = creative.getValueFromSegment(destinationSegment);
                    } else {
                        destinationEnigma = '721793v'; //use chicago as default
                    }
                }
                //makes the final feedURL path
                var feedUrl = creative.getFeedUrl(feedEndpoint, destinationEnigma);
                console.log("Feed Loading; DESTINATION_ENIGMA NOT present; url : " + myFT.instantAds.feedEndpoint);
                //LOAD THE FEED
                var ajaxSet = {
                    complete: function(request) {
                        console.log('complete request');
                        if(request.status === 200) {
                            creative.feedLoaded(request.responseText,myFT.instantAds.feedEndpoint );
                        }
                    },
                    error: function(e) {
                        console.log(e);
                        creative.feedLoadError('feed failed to load',myFT.instantAds.feedEndpoint );
                    }

                };
                FT.ajax(feedUrl, ajaxSet);
            }else{
                isDefault = true;
                creative.feedLoadError('feed over ride use IA vars',myFT.instantAds.feedEndpoint );
            }

        });
    },
    //weather feed or default loads these elements are needed
    buildText : function(){
    	frame1parent = headline_hold_1.getBoundingClientRect();
    	frame2parent = headline_hold_2.getBoundingClientRect();
        //h1 and h2 are in one div then styled for font difference
        h_1_frm_1.innerHTML = creative.checkForCity(myFT.instantAds.frame1_headline_1);
        if(myFT.instantAds.frame1_headline_1_XYOffset !== "" && myFT.instantAds.frame1_headline_1_XYOffset !== "0,0"){
        	rec = h_1_frm_1.getBoundingClientRect();
            h_1_frm_1.style.left = (rec.left - frame1parent.left) + Number(myFT.instantAds.frame1_headline_1_XYOffset.split(",")[0]) + "px";
            h_1_frm_1.style.top = (rec.top - frame1parent.top) + Number(myFT.instantAds.frame1_headline_1_XYOffset.split(",")[1]) + "px";
        }
        h_2_frm_1.innerHTML = creative.checkForCity(myFT.instantAds.frame1_headline_2);
        if(myFT.instantAds.frame1_headline_2_XYOffset !== "" && myFT.instantAds.frame1_headline_2_XYOffset !== "0,0"){
        	rec = h_2_frm_1.getBoundingClientRect();
            h_2_frm_1.style.left = (rec.left - frame1parent.left) + Number(myFT.instantAds.frame1_headline_2_XYOffset.split(",")[0])+"px";
            h_2_frm_1.style.top = (rec.top - frame1parent.top) + Number(myFT.instantAds.frame1_headline_2_XYOffset.split(",")[1])+"px";
        }
        h_3_frm_1.innerHTML = creative.checkForCity(myFT.instantAds.frame1_headline_3);
        if(myFT.instantAds.frame1_headline_3_XYOffset !== "" && myFT.instantAds.frame1_headline_3_XYOffset !== "0,0"){
        	rec = h_3_frm_1.getBoundingClientRect();
            h_3_frm_1.style.left = (rec.left - frame1parent.left) + Number(myFT.instantAds.frame1_headline_3_XYOffset.split(",")[0])+"px";
            h_3_frm_1.style.top = (rec.top - frame1parent.top) + Number(myFT.instantAds.frame1_headline_3_XYOffset.split(",")[1])+"px";
        }

        headline_hold_1.style.color = myFT.instantAds.default_copy_color;
        if(myFT.instantAds.default_copy_color.toUpperCase() === "#FFF"){
            h_1_frm_1.style.textShadow = "none";
            h_2_frm_1.style.textShadow = "none";
            h_3_frm_1.style.textShadow = "none";
            h_1_frm_2.style.textShadow = "none";
            h_2_frm_2.style.textShadow = "none";
            h_3_frm_2.style.textShadow = "none";
        }
        //VAR ADJUST LEFT/TOP for HEADERS POSITION FOR ENTIRE BLOCK
        if(myFT.instantAds.frame1_headlines_XYOffset !== "" && myFT.instantAds.frame1_headlines_XYOffset !== "0,0"){
        	rec = headline_hold_1.getBoundingClientRect();
            headline_hold_1.style.left = rec.left + Number(myFT.instantAds.frame1_headlines_XYOffset.split(",")[0]) + "px";
            headline_hold_1.style.top = rec.top + Number(myFT.instantAds.frame1_headlines_XYOffset.split(",")[1]) + "px";
        }

        //logo_frm1 -- travel_logo1_XYOffset -- travel_logo2_XYOffset
        if(myFT.instantAds.travel_logo1_XYOffset !== "" && myFT.instantAds.travel_logo1_XYOffset !== "0,0"){
            rec = logo_frm1.getBoundingClientRect();
            logo_frm1.style.left = rec.left + Number(myFT.instantAds.travel_logo1_XYOffset.split(",")[0]) + "px";
            logo_frm1.style.top = rec.top + Number(myFT.instantAds.travel_logo1_XYOffset.split(",")[1]) + "px";
        }
        //FRAME 2
        h_1_frm_2.innerHTML = "<p><span class='sb_xCondMed'>"+creative.checkForCity(myFT.instantAds.frame2_headline_1)+"</span><br>";
        if(myFT.instantAds.frame2_headline_1_XYOffset !== "" && myFT.instantAds.frame2_headline_1_XYOffset !== "0,0"){
        	rec = h_1_frm_2.getBoundingClientRect();
            h_1_frm_2.style.left = (rec.left - frame2parent.left) + Number(myFT.instantAds.frame2_headline_1_XYOffset.split(",")[0]) + "px";
            h_1_frm_2.style.top = (rec.top - frame2parent.top) + Number(myFT.instantAds.frame2_headline_1_XYOffset.split(",")[1]) + "px";
        }
        h_2_frm_2.innerHTML = "<span class='sb_xCondMed'>"+creative.checkForCity(myFT.instantAds.frame2_headline_2)+"</span>";
        if(myFT.instantAds.frame2_headline_2_XYOffset !== "" && myFT.instantAds.frame2_headline_2_XYOffset !== "0,0"){
        	rec = h_2_frm_2.getBoundingClientRect();
            h_2_frm_2.style.left = (rec.left - frame2parent.left) + Number(myFT.instantAds.frame2_headline_2_XYOffset.split(",")[0]) + "px";
            h_2_frm_2.style.top = (rec.top - frame2parent.top) + Number(myFT.instantAds.frame2_headline_2_XYOffset.split(",")[1]) + "px";
        }
        h_3_frm_2.innerHTML = "<br><span class='bs_bold' '>"+creative.checkForCity(myFT.instantAds.frame2_headline_3)+"</span></p>";
        if(myFT.instantAds.frame2_headline_3_XYOffset !== "" && myFT.instantAds.frame2_headline_3_XYOffset !== "0,0"){
        	rec = h_3_frm_2.getBoundingClientRect();
            h_3_frm_2.style.left = (rec.left - frame2parent.left) + Number(myFT.instantAds.frame2_headline_3_XYOffset.split(",")[0]) + "px";
            h_3_frm_2.style.top = (rec.top - frame2parent.top) + Number(myFT.instantAds.frame2_headline_3_XYOffset.split(",")[1]) + "px";
        }
        headline_hold_2.style.color = myFT.instantAds.default_copy_color;
        //VAR ADJUST LEFT/TOP for HEADERS POSITION FOR ENTIRE BLOCK
        if(myFT.instantAds.frame2_headlines_XYOffset !== "" && myFT.instantAds.frame2_headlines_XYOffset !== "0,0"){
        	rec = headline_hold_2.getBoundingClientRect();
            headline_hold_2.style.left = rec.left + Number(myFT.instantAds.frame2_headlines_XYOffset.split(",")[0]) + "px";
            headline_hold_2.style.top = rec.top + Number(myFT.instantAds.frame2_headlines_XYOffset.split(",")[1]) + "px";
        }
        //cta
        cta_copy.innerHTML = myFT.instantAds.finalFrame_CTA_copy;
        if(myFT.instantAds.finalFrame_CTA_XYOffset !== "" && myFT.instantAds.finalFrame_CTA_XYOffset !== "0,0"){
            rec = cta_hold.getBoundingClientRect();
            cta_hold.style.left = (rec.left) + Number(myFT.instantAds.finalFrame_CTA_XYOffset.split(",")[0]) + "px";
            cta_hold.style.top = (rec.top) + Number(myFT.instantAds.finalFrame_CTA_XYOffset.split(",")[1]) + "px";
        }
        rec = cta_copy.getBoundingClientRect();
        cta_hold.style.width = (rec.width+8)+"px";
        cta_copy.style.width = (rec.width+8)+"px";
        if(navigator.userAgent.indexOf('MSIE')!==-1
            || navigator.appVersion.indexOf('Trident/') > 0){
            /* Microsoft Internet Explorer detected in. */
            cta_copy.style.paddingTop = '7px';
        }
        //disclaimer text
        disclaimer.innerHTML = myFT.instantAds.disclaimerText;
        if(myFT.instantAds.diclaimerText_XYOffset !== "" && myFT.instantAds.diclaimerText_XYOffset !== "0,0"){
            rec = disclaimer.getBoundingClientRect();
            disclaimer.style.left = (rec.left) + Number(myFT.instantAds.diclaimerText_XYOffset.split(",")[0]) + "px";
            disclaimer.style.top = (rec.top) + Number(myFT.instantAds.diclaimerText_XYOffset.split(",")[1]) + "px";
        }
        creative.addListeners();
    },

    addListeners : function(){
        if(isDefault){
            myFT.applyButton(btn, creative.onCT_1_default);
        }else{
            myFT.applyButton(btn, creative.onCT_1);
        }
        creative.goBanner();
    },

    //FEED SUCCESS
    feedLoaded : function(feedItems, feedUrl) {
        console.log("Feed Success ; url : " + feedUrl);
        feedReturned = true;
        //feedReturned is set to true to let
        if (window.DOMParser) {
            parser=new DOMParser();
            xmlDoc=parser.parseFromString(feedItems,"text/xml");
        } else {
            xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
            xmlDoc.async=false;
            xmlDoc.loadXML(feedItems);
        }
        cityNm = xmlDoc.getElementsByTagName("destination")[0].childNodes[0].nodeValue.toUpperCase();
        prodURL = xmlDoc.getElementsByTagName("destination_url")[0].childNodes[0].nodeValue;
        console.log("prodURL : " + prodURL);
        var imgURL = xmlDoc.getElementsByTagName("image_728_a")[0].childNodes[0].nodeValue;
        //console.log('img url ;: ', imgURL);
        TweenLite.delayedCall(.1, creative.checkReadyStatus);
        var imgA = [
            {ia:myFT.instantAds.travel_logo, id: "logo_frm1"},
            {ia:imgURL, id: "hero"}
        ];
        creative.loadImgs(imgA);

    },
    //FEED FAILURE
    feedLoadError : function(errorMsg, feedUrl) {
        console.log('Feed FAIL OR DEFAULT: ',errorMsg);
        //console.log('img url ;: ', imgURL);
        prodURL = myFT.instantAds.clickThroughURL;
        TweenLite.delayedCall(.1, creative.checkReadyStatus);
        var imgA = [

            {ia:myFT.instantAds.travel_logo, id: "logo_frm1"},
            {ia:myFT.instantAds.image_default, id: "hero"}
        ];

        isDefault = true;
        creative.loadImgs(imgA);
        feedReturned = true;
    },
    //START AD
    goBanner : function(){
    	if(myFT.instantAds.firePixels == "true" || myFT.instantAds.firePixels == "TRUE") {
			productClicked = new Image();
			productClicked.src = myFT.instantAds.pixelURL;
		}
		
        TweenLite.to(container,0,{opacity:1});
        TweenLite.to(frm_1,1.2, {opacity:1, delay:1});
        TweenLite.to(frm_1, 0.85,{opacity:"0", delay:4.2});
        TweenLite.to(frm_2, 0.85,{opacity:"1", delay:4.7});
        TweenLite.from(h_1_frm_2,.65,{opacity:0, delay:5.7});
        TweenLite.from(h_2_frm_2,.65,{opacity:0, delay:5.7});
        TweenLite.from(h_3_frm_2,1.25,{left:"-60px", opacity:0,delay:6.6}); /**/
        
        TweenLite.from(cta_hold,.65,{opacity:0, delay:8, onComplete:function() {
        	creative.triggerShimmer();
        	container.addEventListener("mouseover", creative.triggerShimmer);
        }});
    },
    //LOAD IMAGES
    loadImgs : function(allImgs){
        var tmpCnt = 0;
        //console.log('retrunFunc is ::  ',retrunFunc);
        for(var i = 0; i < allImgs.length; i++){
            var elm = document.getElementById(allImgs[i].id);
            //	console.log('length ',allImgs.length);
            //	console.log('elm id is',allImgs[i].id);
            elm.onload = function(e){
                tmpCnt++;
                //  	console.log('loadImgs :: tmpCnt : ', tmpCnt);
                if( tmpCnt === allImgs.length) {
                    imagesLoaded = true;
                }

            };
            elm.src = allImgs[i].ia;
        }
    },

    checkForCity : function(s){
        var rs = s.replace('[%CITY%]',cityNm);
        return rs;
    },

    checkReadyStatus : function(){
        if(feedReturned && imagesLoaded){
            creative.buildText();
        }else{
            TweenLite.delayedCall(.1, creative.checkReadyStatus);
        }
    },

    onCT_1 : function(){
        myFT.clickTag(1, prodURL);
    },
	onCT_1_default : function(){
        myFT.clickTag(1, myFT.instantAds.clickThroughURL);
    },
    getFeedUrl : function(feedEndpoint, destinationEnigma){
        serveDom = myFT.get("serveDom") || "http://cdn.flashtalking.com";
        var protocol = (serveDom.indexOf("https://")>-1)?"https://":"http://";
        var url = feedEndpoint.split('[%PROTOCOL%]').join(protocol);
        url = url.split('[%SERVE_DOM%]').join(serveDom);
        url = url.split('[%CACHEBUSTER%]').join(Math.floor(Math.random()*9e9));
        url = url.split('[%DESTINATION_ENIGMA%]').join(destinationEnigma);
        return url;
    },

    getValueFromSegment : function(segment){
        var ptn = new RegExp(segment + '([a-zA-Z0-9_]+?)(,|$)');
        var segString = myFT.get("ftSegment");
        return segString.match(ptn)[1];
    },

    checkSegmentInParam : function(seg) {
        if((myFT.get("ftSegment")) && myFT.get("ftSegment").indexOf(seg)>=0) {
            return true;
        } else {
            return false;
        }
    },
    
    triggerShimmer : function() {
    	var tweenTo = cta_hold.getBoundingClientRect().width;
    	TweenLite.to(shimmer, 1, {left:tweenTo, onComplete: function() {
    		shimmer.style.left = "-111px";
    	}, overwrite:0});
    }
};

creative.init();