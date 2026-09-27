/**
 * DIT University Editorial Board - Pratibimb '25
 * Complete spread catalog and table of contents mapping
 */

const MAGAZINE_METADATA = {
  title: "Pratibimb '25",
  subtitle: "Reflection of Innovation",
  edition: "27th Edition",
  institution: "DIT University, Dehradun",
  established: 1998,
  totalSpreads: 68,
  totalPages: 135,
  pdfUrl: "pratibimb2025.pdf", // If local or hosted
};

const SECTIONS = [
  { id: "cover", title: "Cover & In Brief", spread: 0, page: 1, icon: "sparkles" },
  { id: "board", title: "Editorial Board", spread: 1, page: 2, icon: "users" },
  { id: "desk", title: "From the Desk", spread: 4, page: 8, icon: "feather" },
  { id: "central", title: "Central News", spread: 7, page: 14, icon: "landmark" },
  { id: "departments", title: "Department News", spread: 27, page: 54, icon: "layers" },
  { id: "clubs", title: "Club News", spread: 35, page: 70, icon: "compass" },
  { id: "placements", title: "Placements & Honors", spread: 38, page: 76, icon: "award" },
  { id: "alumni", title: "Alumni Spotlight", spread: 41, page: 82, icon: "globe" },
  { id: "research", title: "Research & Patents", spread: 42, page: 84, icon: "book-open" },
  { id: "articles", title: "Articles & Essays", spread: 55, page: 110, icon: "file-text" },
  { id: "creatives", title: "Creatives & Gallery", spread: 60, page: 120, icon: "palette" },
  { id: "backcover", title: "Back Cover", spread: 67, page: 134, icon: "bookmark" }
];

const EDITORIAL_TEAM = [
  {
    role: "Editor-in-Chief",
    name: "Dr. Sakshi Semwal",
    department: "Department of Humanities & Social Sciences",
    message: "Pratibimb 2025 has come together through teamwork, patience, and consistent effort. Platforms like this help students discover their voice."
  },
  {
    role: "Student Editor",
    name: "Mahika Maheshwari",
    department: "Editorial Board Leadership"
  },
  {
    team: "Design Team",
    head: "Sanskriti",
    coHead: "Eklavya",
    members: ["Jhanvi", "Samriddhi", "Sakshi", "Tanya", "Jannat", "Ridhi", "Pranjal", "Ryo", "Pranach", "Pragya", "Manosh"]
  },
  {
    team: "Social Media Team",
    head: "Daksh Walia",
    coHead: "Nayonika Dhuria",
    featuredMember: "Tanishq Pandey",
    members: ["Tanishq Pandey", "Janiya", "Kansal", "Manya Verma", "Pragya", "Amusa Chaudhary", "Manosh", "Ishan", "Tanisha Thapa"]
  },
  {
    team: "Content Team",
    head: "Amandeep Kaur",
    coHead: "Apurva Chaudhary",
    members: ["Pavilhi Verma", "Rishwarya", "Rehan", "Averalh Thapa", "Janiya", "Nayanika Dhuria", "Ishaan Sharma", "Jahanvi", "Angela Agarwal"]
  },
  {
    team: "Proof-reading Team",
    head: "Martina",
    coHead: "Aviral",
    members: ["Shraddha", "Saumya", "Akshat", "Tanvi", "Taniya", "Mahima", "Sayita", "Alfiya", "Taruna"]
  }
];

// Helper function to build spread descriptors
const SPREADS = [];
for (let i = 0; i < 68; i++) {
  let title = "";
  let section = "General";
  let pagesLabel = "";

  if (i === 0) {
    title = "Cover — Pratibimb '25 (Reflection of Innovation)";
    section = "Cover";
    pagesLabel = "Cover";
  } else if (i === 1) {
    title = "Editor-in-Chief In Brief & Student Editor";
    section = "Editorial Board";
    pagesLabel = "Pages 2–3";
  } else if (i === 2) {
    title = "Design Team & Social Media Team";
    section = "Editorial Board";
    pagesLabel = "Pages 4–5";
  } else if (i === 3) {
    title = "Content Team & Proof-reading Team";
    section = "Editorial Board";
    pagesLabel = "Pages 6–7";
  } else if (i === 4) {
    title = "Table of Contents & Shri Anuj Agarwal (President)";
    section = "From the Desk";
    pagesLabel = "Pages 8–9";
  } else if (i >= 5 && i <= 6) {
    title = "Leadership Messages from the Desk";
    section = "From the Desk";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 7 && i <= 26) {
    title = "Central University News & Celebrations";
    section = "Central News";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 27 && i <= 34) {
    title = "Departmental Chronicles & Milestones";
    section = "Department News";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 35 && i <= 37) {
    title = "Student Clubs, Societies & Cultural Life";
    section = "Club News";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 38 && i <= 40) {
    title = "Placements, Top Offers & Student Honors";
    section = "Placements & Honors";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i === 41) {
    title = "Alumni Chronicles & Distinguished Leaders";
    section = "Alumni";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 42 && i <= 54) {
    title = "Research Papers, Patents & Innovations";
    section = "Research & Innovation";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 55 && i <= 59) {
    title = "Articles, Thought Pieces & Critical Perspectives";
    section = "Articles";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i >= 60 && i <= 66) {
    title = "Creative Corner, Fine Arts & Visual Poetry";
    section = "Creatives & Gallery";
    pagesLabel = `Pages ${i * 2}–${i * 2 + 1}`;
  } else if (i === 67) {
    title = "Valedictory & Back Cover";
    section = "Back Cover";
    pagesLabel = "Pages 134–135";
  }

  const file = `spread-${String(i).padStart(3, '0')}.jpg`;
  SPREADS.push({
    index: i,
    file: file,
    url: `assets/spreads/${file}`,
    title: title,
    section: section,
    pagesLabel: pagesLabel,
    leftPageNum: i === 0 ? null : i * 2,
    rightPageNum: i === 0 ? 1 : i * 2 + 1
  });
}
