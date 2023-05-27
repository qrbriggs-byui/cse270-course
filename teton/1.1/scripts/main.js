// Show the meet-greet message on Tue/Thu
// Date.getDay() uses a 0 based index to return the day of the week
var messagedate = new Date();
if (messagedate.getDay() == 2 || messagedate.getDay() == 4) {
  document.querySelector("#meet-greet").classList.add("active");
}

// Get business data for spotlights

const businessDataUrl = "./data/business.json";


function displaySpotlights(businessList){
  businessList = businessList.filter(x => x.membershipLevel == 'gold' || x.membershipLevel == 'silver');
  spotlights = []
  for (let i=0; i < 3; i++){
    var elt = Math.floor(Math.random() * businessList.length)
    spotlights.push(businessList.splice(elt, 1)[0]);
  }

  // Now display stuff  
  var mainspotlight = document.querySelector('.main-spotlight');
  spotlightcount = 1;
  spotlights.forEach((spotlight) => {
    var newdiv = document.createElement('div');
    newdiv.classList.add('spotlight'+spotlightcount);
    spotlightcount++;
    newdiv.innerHTML = `<h4>${spotlight.name}</h4>
                        <p class="centered-image"><a href="${spotlight.websiteURL}"><img src="${spotlight.imageURL}"></a></p>
                        <p>${spotlight.streetAddress}, ${spotlight.cityStateZip}</p>
                        <p><a href="${spotlight.websiteURL}">${spotlight.websiteURL}</a></p>
                        <p>${spotlight.adcopy}</p>`
    mainspotlight.append(newdiv);    
  })
}

async function getBusinessData() {
  const response = await fetch(businessDataUrl);
  if (response.ok) {
    const data = await response.json();
    displaySpotlights(data.businesses);
  } else {
    console.error("There was an error loading the data.");
  }
}

getBusinessData();