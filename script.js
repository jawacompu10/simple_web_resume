document.addEventListener('DOMContentLoaded', () => {
    // Fetch and read the json file
    fetch('resume.json')
        .then(response => response.json())
        .then(data => populateResume(data))
        .catch(error => console.error('Error fetching resume.json:', error));
});

function populateResume(data) {
    // Header
    const personalInfo = data.personalInfo || {};
    document.getElementById('name').textContent = personalInfo.name || '';
    document.getElementById('title').textContent = personalInfo.title || '';
    document.getElementById('branding').textContent = personalInfo.branding || '';
    document.getElementById('summary').textContent = data.summary || '';
    
    // Contact Bar
    document.getElementById('email').textContent = personalInfo.email || '';
    document.getElementById('phone').textContent = personalInfo.phone || '';
    
    if (personalInfo.github) {
        let githubUrl = personalInfo.github;
        document.getElementById('github').href = githubUrl;
    }
    if (personalInfo.linkedin) {
        let linkedinUrl = personalInfo.linkedin;
        document.getElementById('linkedin').href = linkedinUrl;
    }
    
    // Work Experience
    const experienceList = document.getElementById('experience-list');
    if (data.experience && data.experience.length > 0) {
        experienceList.innerHTML = '';
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

    // Skills
    const skillsList = document.getElementById('skills-list');
    if (data.skills) {
        skillsList.innerHTML = '';
        for (let category in data.skills) {
            const categoryDiv = document.createElement('span');
            categoryDiv.className = 'skill-category';
            
            const categoryName = document.createElement('span');
            categoryName.className = 'skill-category-name';
            // Convert camelCase to Title Space e.g. qualityEngineering -> Quality Engineering
            categoryName.textContent = category.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
            
            const categorySkills = document.createElement('span');
            categorySkills.className = 'skill-category-items';
            categorySkills.innerHTML = data.skills[category].join('<br>');
            
            categoryDiv.appendChild(categoryName);
            categoryDiv.appendChild(categorySkills);
            skillsList.appendChild(categoryDiv);
        }
    }

    // Education
    const educationList = document.getElementById('education-list');
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

    // Key Achievements
    if (data.keyAchievements && data.keyAchievements.length > 0) {
        document.getElementById('key-achievements-section').style.display = 'block';
        const achievementsList = document.getElementById('key-achievements-list');
        data.keyAchievements.forEach(achievement => {
            const li = document.createElement('li');
            li.textContent = achievement;
            achievementsList.appendChild(li);
        });
    }

    // Project Highlights
    if (data.projectHighlights && data.projectHighlights.length > 0) {
        document.getElementById('project-highlights-section').style.display = 'block';
        const highlightsList = document.getElementById('project-highlights-list');
        data.projectHighlights.forEach(highlight => {
            const li = document.createElement('li');
            li.textContent = highlight;
            highlightsList.appendChild(li);
        });
    }
}
