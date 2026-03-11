// Initialize Dexie.js database
const db = new Dexie("ResumeDB");

// Define schema: one table for profiles
db.version(1).stores({
  profiles: '++id, name, title, lastModified'
});

async function getAllProfiles() {
    return await db.profiles.toArray();
}

async function getProfile(id) {
    return await db.profiles.get(Number(id));
}

async function saveProfile(profile) {
    profile.lastModified = new Date().toISOString();
    return await db.profiles.put(profile);
}

async function deleteProfile(id) {
    return await db.profiles.delete(Number(id));
}

function downloadProfileAsJson(profile) {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(profile, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    const fileName = (profile.personalInfo?.name || "resume").replace(/\s+/g, '_').toLowerCase() + ".json";
    downloadAnchorNode.setAttribute("download", fileName);
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}
