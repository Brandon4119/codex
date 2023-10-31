let projects;
let experience;

// LETS GET THE DATA
fetch('../data/projects.json').then(response => {
    // "We got the the response now what?"
    return response.json();

    // CREATE THE PROJECT CARDS
}).then(createProjectCard);

fetch('./data/experience.json').then(response => response.json()).then(createExperienceCards);

function createProjectCard(json) {
    projects = json;

    const projectsListElement = document.getElementById("projects-list");

    const projectsSize = projects.length;

    // ADD THE CARDS TO THE HTML
    for (let i=0; i < projectsSize ; i++){
        projectsListElement.innerHTML += `
        <div class="project-card">
        <a href="${projects[i].repository}" alt="">
            <img src="${projects[i].img}" alt="">

            <p>${projects[i].name}</p>
            <p>${projects[i].description}</p>
            <p>${projects[i].year}</p>

            <div id="technology-${i}" class="technologies center">

            </div>
        </a>
    </div>
        `;

        const technologiesElement = document.getElementById(`technology-${i}`);
        const technologiesSize = projects[i].technologies.length;

        for (let j = 0; j < technologiesSize ; j++) {
            technologiesElement.innerHTML += `
            <label>${projects[i].technologies[j]})</label>
            `;
        }
    }
}

function createExperienceCards(json) {
    experience = json;

    const experienceListElement = document.getElementById("experience-list");
    const experienceSize = experience.length;

    for (let i = 0; i < experienceSize; i ++) {
        // ADD THE CARD
        experienceListElement.innerHTML += `
        <div class="experience-card">
        <p>${experience[i].entity}</p>
        <p>${experience[i].title}</p>
        <p>${experience[i].description}</p>
        <p>${experience[i].period}</p>

        <div class="technologies">
            <label>Technology</label>
            <label>Or</label>
            <label>Skill</label>
        </div>
    </div>
        `;

        const technologySkillElement = document.getElementById(`technology-skill-${i}`);
        const technologySkillSize = experience[i].technology.length;

        for ( let j = 0; j < technologySkillSize; j ++) {
            technologySkillElement.innerHTML += `
                <label>${experience[i].technology[j]}</label>
            `;
        }
    }
}