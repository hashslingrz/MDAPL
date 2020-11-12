/**
 * Set up TryAPL Execution Buttons
 */

const runWhenDOMLoadedTryAPL = tryaplbtn => {
  if (document.readyState != 'loading') {
    tryaplbtn()
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', tryaplbtn)
  } else {
    document.attachEvent('onreadystatechange', function() {
      if (document.readyState == 'complete') tryaplbtn()
    })
  }
}

const addTryAPLButtonToCodeCells = () => {    
    // Add TryAPL buttons to all of our code cells
    const codeCells = document.querySelectorAll('div.highlight pre')
    codeCells.forEach((codeCell, index) => {
        const id =  `codecell${index}`
        codeCell.setAttribute('id', id)
        const pre_bg = getComputedStyle(codeCell).backgroundColor

        const tryapl_link = `?clear&q=${encodeURIComponent((codeCell.innerText).trim())}&run`

        const clipboardButton = id =>
        `<a class="copybtn" style="background-color: ${pre_bg}" href="https://staging.tryapl.org/${tryapl_link}">
        <img src="${DOCUMENTATION_OPTIONS.URL_ROOT}_static/tryapl.svg" alt="Run code on TryAPL">
        </a>`
        codeCell.insertAdjacentHTML('afterend', clipboardButton(id))
    })
    
    // <span> button container
    const cellContainers = document.querySelectorAll('div.highlight')
    cellContainers.forEach((containerCell, index) => {
        const btncontainer = document.createElement('span');
        btncontainer.setAttribute('class', 'btncontainer');
        const code_btns = containerCell.querySelectorAll('a.copybtn')
        code_btns.forEach((copybtn, idx) => {
          btncontainer.appendChild(copybtn)
        })
        containerCell.appendChild(btncontainer)
    })
}

runWhenDOMLoadedTryAPL(addTryAPLButtonToCodeCells)