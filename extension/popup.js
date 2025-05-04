console.log("Popup script loaded");
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      func: async () => {
        console.log("Executing script in the page context");
        const div = document.querySelector('.ui-card-content');
        if (div) { 
            const paragraphs = div.querySelectorAll('p');
            const textElements = Array.from(paragraphs).map(p => p.textContent.trim());
            // const text = textElements.join(',');
            //I used during testing to see the text elements
            // console.log(textElements);
            // console.log(textElements.length);
            const response = await fetch('http://127.0.0.1:8000/api/', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(textElements.slice(0, textElements.length - 3))
            });
            const data = await response.json();
            
            
            return data;

    }
}
 }
).then(answer => {
    document.getElementById("content").textContent = answer[0].result;

})




  }
);




// setTimeout(() => {
//     console.log("Executed after 1 second");
//     const s = document.getElementById("content");
//     s.innerHTML = "Hello World!";

//   }, 2000);
  



