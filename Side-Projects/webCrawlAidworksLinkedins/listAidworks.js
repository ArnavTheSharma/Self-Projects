const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'listAidworks.json');

const members = [
    {
        name: "Trung Nguyen",
        position: "Chief Executive Officer",
        bio: "I'm Trung, a sophomore in college who is passionate about managing non-profits, finances, and benefiting society."
    },
    {
        name: "Krish Jain",
        position: "Chief Information Officer",
        bio: "I'm Krish, a sophomore in college who enjoys coding, teaching, and giving back to the community."
    },
    {
        name: "Aadi Dixit",
        position: "Chief Compliance Officer",
        bio: "I'm Aadi, a freshman in college who loves to problem-solve and help others within our community."
    },
    {
        name: "Madhavan Rajagopalan",
        position: "Chief Operating Officer",
        bio: "I'm Madhavan, a sophomore in college who is passionate about helping the community and managing volunteers."
    },
    {
        name: "Siddh Patel",
        position: "Deputy Chief of Human Resources Officer",
        bio: "I'm Siddh, a sophomore in college who enjoys outdoor activities, talking, and helping out my community."
    },
    {
        name: "Brian Olsen",
        position: "Head of Volunteering",
        bio: "I'm Brian, a high school senior passionate about basketball, golf, education, and helping others."
    },
    {
        name: "Ishan Jain",
        position: "Head of Finance",
        bio: "I'm Ishan, a high school senior passionate about giving back to communities, having fun, and designing my own CAD projects."
    },
    {
        name: "Emily Chow",
        position: "Head of Marketing",
        bio: "I'm Emily, a high school senior, musician, and rhythmic gymnastics coach who aims to create a more uplifting community!"
    },
    {
        name: "Satya Divakaruni",
        position: "Head of Public Health",
        bio: "I'm Satya, a junior in high school and I enjoy helping others through various different community service projects and campaigns."
    },
    {
        name: "Arnav Sharma",
        position: "Head of Technology",
        bio: "I'm Arnav, a sophomore in college who enjoys coding, tennis and learning how things work."
    },
    {
        name: "Raghu Rajagopalan",
        position: "Director of Food Security",
        bio: "I'm Raghu, a high school sophomore passionate about volunteering and enthusiastic about helping our community."
    },
    {
        image: null,
        name: "Adi Kinhikar",
        position: "Volunteering Department",
        bio: ""
    },
    {
        image: null,
        name: "Emad Makhdumi",
        position: "Volunteering Department",
        bio: ""
    },
    {
        image: null,
        name: "Katherine",
        position: "Marketing Department",
        bio: ""
    },
    {
        name: "Advith Velamakanni",
        position: "Marketing Department",
        bio: "I'm Advith, a junior in college passionate about filmmaking, fencing, and supporting our community."
    },
    {
        name: "Connor Duffy",
        position: "Marketing Department",
        bio: "I'm Connor, a junior in college who is passionate about fostering positivity and hope through community service and outreach."
    },
    {
        name: "Pratap Srivastava",
        position: "Marketing Department",
        bio: "I'm Pratap, an high school senior who loves playing piano, cars, aviation, and staying active."
    },
    {
        name: "Gayatri Iyer",
        position: "Finance Department",
        bio: "I'm Gayatri, a high school senior who is very interested in volunteering, community service, and business & finance projects."
    },
    {
        name: "Aarya Deepak",
        position: "Finance Department",
        bio: "I'm Aarya, a freshman in college who loves helping out his local community through fundraising and volunteering."
    },
    {
        name: "Mahesh Manneru",
        position: "Finance Department",
        bio: "I'm Mahesh, a high school senior who loves to code and play chess. I want to make a good change in our community."
    },
    {
        name: "Raashid Abdullah",
        position: "Public Health Department",
        bio: "I'm Raashid, a high school senior who loves to do art, is ecstatic about biology, and likes to volunteer to give back to the community."
    },
    {
        name: "Shreya Saikia",
        position: "Public Health Department",
        bio: "Hi my name is Shreya and I am excited to be apart of a community that’s passionate about public health!"
    },
    {
        name: "Katherine Mui",
        position: "Public Health Department",
        bio: "Hi I’m Katherine. I’m passionate about helping our community and I’m excited to be apart of TAWF!"
    },
    {
        name: "Lillian Wen",
        position: "Public Health Department",
        bio: "I’m Lillian, a senior passionate about public health and committed to supporting community wellness through education and outreach."
    },
];


const members2 = members.map(e => e.name);
const jsonString = JSON.stringify(members2);

fs.writeFileSync(filePath, jsonString, 'utf8');
console.log(members2);

module.exports = members2;
