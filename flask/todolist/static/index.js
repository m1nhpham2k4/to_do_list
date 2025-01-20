const deleteNote = (noteID) => {
    console.log(noteID)
    fetch("/delete-note",{
        method: "POST",
        body: JSON.stringify({note_id: noteID}),
    }).then( (response) =>{
        window.location.href = '/';
    })
}