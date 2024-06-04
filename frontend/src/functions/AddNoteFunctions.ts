function getNoteData(formData: any) {
    return {
        create_date: formData.create_date,
        modification_date: formData.modification_date,
        note_text: formData.note_text,
        child: formData.child_id,
    };
}

export { getNoteData };
