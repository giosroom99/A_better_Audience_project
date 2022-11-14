// Giovanni Tshibangu


function changeTheme() {
 
    const theme = document.getElementsByTagName('link')[0];

    // Change the value of href attribute 
    // to change the css sheet.
    if (theme.getAttribute('href') == 'dark-blue.css') {
        theme.setAttribute('href', 'dark-blue.css');
    } else {
        theme.setAttribute('href', '.css/light-orange.css');
    }
}

console.log('tttttttttttt')