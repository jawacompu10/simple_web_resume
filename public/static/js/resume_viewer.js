document.addEventListener('DOMContentLoaded', async () => {
    const container = document.querySelector('.resume-container');
    const profileId = container ? container.getAttribute('data-profile-id') : null;

    if (profileId && profileId !== "None" && profileId !== "") {
        try {
            const data = await getProfile(profileId);
            if (data) {
                populateResume(data);
                checkAutoPrint();
            } else {
                console.error('Profile not found in DB:', profileId);
            }
        } catch (error) {
            console.error('Error fetching profile from DB:', error);
        }
    } else {
        // Fallback to JSON
        fetch('/static/resume.json')
            .then(response => response.json())
            .then(data => {
                populateResume(data);
                checkAutoPrint();
            })
            .catch(error => console.error('Error fetching resume.json:', error));
    }
});

function checkAutoPrint() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('print') === 'true') {
        // Wait a tiny bit for all images/fonts to definitely settle, though text is already there
        setTimeout(() => window.print(), 500);
    }
}

function populateResume(data) {
    // Header
    const personalInfo = data.personalInfo || {};
    // Use scoped selectors if possible to avoid conflicts, or just trust the IDs in resume_layout.html
    const getName = () => document.querySelector('.resume-container #name') || document.getElementById('name');
    const getTitle = () => document.querySelector('.resume-container #title') || document.getElementById('title');
    const getBranding = () => document.querySelector('.resume-container #branding') || document.getElementById('branding');
    const getSummary = () => document.querySelector('.resume-container #summary') || document.getElementById('summary');
    
    if (getName()) getName().textContent = personalInfo.name || '';
    if (getTitle()) getTitle().textContent = personalInfo.title || '';
    if (getBranding()) getBranding().textContent = personalInfo.branding || '';
    if (getSummary()) getSummary().textContent = data.summary || '';
    
    // Contact Bar
    const getEmail = () => document.querySelector('.resume-container #email') || document.getElementById('email');
    const getPhone = () => document.querySelector('.resume-container #phone') || document.getElementById('phone');
    const getLocation = () => document.querySelector('.resume-container #location') || document.getElementById('location');
    
    if (getEmail()) getEmail().textContent = personalInfo.email || '';
    if (getPhone()) getPhone().textContent = personalInfo.phone || '';
    if (getLocation()) getLocation().textContent = personalInfo.currentLocation || '';
    
    const getGithub = () => document.querySelector('.resume-container #github') || document.getElementById('github');
    const getLinkedin = () => document.querySelector('.resume-container #linkedin') || document.getElementById('linkedin');
    const getWebsite = () => document.querySelector('.resume-container #website') || document.getElementById('website');
    const getWebsiteContainer = () => document.querySelector('.resume-container #website-container') || document.getElementById('website-container');

    if (getGithub()) {
        getGithub().href = personalInfo.github || '#';
    }
    if (getLinkedin()) {
        getLinkedin().href = personalInfo.linkedin || '#';
    }
    if (getWebsite()) {
        if (personalInfo.website) {
            getWebsite().href = personalInfo.website;
            if (getWebsiteContainer()) getWebsiteContainer().style.display = 'inline';
        } else {
            if (getWebsiteContainer()) getWebsiteContainer().style.display = 'none';
        }
    }
    
    // Work Experience
    const experienceList = document.querySelector('.resume-container #experience-list') || document.getElementById('experience-list');
    if (experienceList) {
        experienceList.innerHTML = '';
        if (data.experience && data.experience.length > 0) {
            const recentExp = data.experience.slice(0, 6);
            const olderExp = data.experience.slice(6);

            recentExp.forEach(job => {
                const expItem = document.createElement('div');
                expItem.className = 'experience-item';

                const expHeader = document.createElement('div');
                expHeader.className = 'experience-header';
                
                const titleDiv = document.createElement('div');
                titleDiv.innerHTML = `<div class="job-title">${job.title} &mdash; <span class="job-company">${job.company}</span></div>`;
                
                const metaDiv = document.createElement('div');
                metaDiv.className = 'job-meta';
                metaDiv.innerHTML = `<span>${job.years}</span>`;

                expItem.appendChild(titleDiv);
                expItem.appendChild(metaDiv);
                
                if (job.description && job.description.length > 0) {
                    const ul = document.createElement('ul');
                    ul.className = 'job-desc';
                    job.description.forEach(desc => {
                        const li = document.createElement('li');
                        li.textContent = desc;
                        ul.appendChild(li);
                    });
                    expItem.appendChild(ul);
                }
                
                experienceList.appendChild(expItem);
            });

            if (olderExp.length > 0) {
                const earlierHeader = document.createElement('h4');
                earlierHeader.textContent = 'Earlier Experience';
                earlierHeader.className = 'earlier-exp-title';
                experienceList.appendChild(earlierHeader);

                const ul = document.createElement('ul');
                ul.className = 'earlier-exp-list';
                olderExp.forEach(job => {
                    const li = document.createElement('li');
                    li.innerHTML = `<strong>${job.title}</strong> &mdash; ${job.company} <em>(${job.years})</em>`;
                    ul.appendChild(li);
                });
                experienceList.appendChild(ul);
            }
        }
    }

    // Skills
    const skillsList = document.querySelector('.resume-container #skills-list') || document.getElementById('skills-list');
    if (skillsList) {
        skillsList.innerHTML = '';
        if (data.skills) {
            for (let category in data.skills) {
                const categoryDiv = document.createElement('span');
                categoryDiv.className = 'skill-category';
                
                const categoryName = document.createElement('span');
                categoryName.className = 'skill-category-name';
                // Convert camelCase to Title Space e.g. qualityEngineering -> Quality Engineering
                categoryName.textContent = category.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
                
                const categorySkills = document.createElement('span');
                categorySkills.className = 'skill-category-items';
                categorySkills.innerHTML = Array.isArray(data.skills[category]) ? data.skills[category].join('<br>') : '';
                
                categoryDiv.appendChild(categoryName);
                categoryDiv.appendChild(categorySkills);
                skillsList.appendChild(categoryDiv);
            }
        }
    }

    // Education
    const educationList = document.querySelector('.resume-container #education-list') || document.getElementById('education-list');
    if (educationList) {
        educationList.innerHTML = '';
        if (data.education && data.education.length > 0) {
            data.education.forEach(edu => {
                const eduItem = document.createElement('div');
                eduItem.className = 'education-item';
                
                eduItem.innerHTML = `
                    <div class="edu-degree">${edu.degree}</div>
                    <div class="edu-university">${edu.university}</div>
                    <div class="edu-date">${edu.years}</div>
                `;
                
                educationList.appendChild(eduItem);
            });
        }
    }

    // Key Achievements
    const achSection = document.querySelector('.resume-container #key-achievements-section') || document.getElementById('key-achievements-section');
    const achList = document.querySelector('.resume-container #key-achievements-list') || document.getElementById('key-achievements-list');
    if (achSection && achList) {
        achList.innerHTML = '';
        if (data.keyAchievements && data.keyAchievements.length > 0) {
            achSection.style.display = 'block';
            data.keyAchievements.forEach(achievement => {
                const li = document.createElement('li');
                li.textContent = achievement;
                achList.appendChild(li);
            });
        } else {
            achSection.style.display = 'none';
        }
    }

    // Project Highlights
    const projSection = document.querySelector('.resume-container #project-highlights-section') || document.getElementById('project-highlights-section');
    const projList = document.querySelector('.resume-container #project-highlights-list') || document.getElementById('project-highlights-list');
    if (projSection && projList) {
        projList.innerHTML = '';
        if (data.projectHighlights && data.projectHighlights.length > 0) {
            projSection.style.display = 'block';
            data.projectHighlights.forEach(highlight => {
                const li = document.createElement('li');
                li.textContent = highlight;
                projList.appendChild(li);
            });
        } else {
            projSection.style.display = 'none';
        }
    }
}
