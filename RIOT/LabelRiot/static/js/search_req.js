const access_token_FS = localStorage.getItem('acc_tok');
console.log('acc_tok', access_token_FS);

const profile = await fetchProfile(access_token_FS);
populateUI(profile);


async function fetchProfile(token) {
    if (token!=undefined){
        localStorage.setItem('acc_tok' , token);
    } 
    console.log('token', token);
    const access_token_FS = localStorage.getItem('acc_tok');
    console.log('acc_tok', access_token_FS);
    const result = await fetch("https://api.spotify.com/v1/me", {
        method: "GET", headers: { Authorization: `Bearer ${access_token_FS}` }
    });

    return await result.json();
}



function populateUI(profile) {
    document.getElementById("displayName").innerText = profile.display_name;
    if (profile.images[0]) {
        const profileImage = new Image(200, 200);
        profileImage.src = profile.images[0].url;
        document.getElementById("avatar").appendChild(profileImage);
        document.getElementById("imgUrl").innerText = profile.images[0].url;
    }
    document.getElementById("id").innerText = profile.id;
    document.getElementById("email").innerText = profile.email;
    document.getElementById("uri").innerText = profile.uri;
    document.getElementById("uri").setAttribute("href", profile.external_urls.spotify);
    document.getElementById("url").innerText = profile.href;
    document.getElementById("url").setAttribute("href", profile.href);
}