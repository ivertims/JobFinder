import axios from 'axios';

const ADZUNA_APP_ID = import.meta.env.VITE_ADZUNA_APP_ID;
const ADZUNA_APP_KEY = import.meta.env.VITE_ADZUNA_APP_KEY;
const BASE_URL = '/api-adzuna/v1/api/jobs/gb/search';

export const fetchJobs = async (keyword = '', location = '', page = 1) => {
  // Use MOCK DATA if API keys are missing or contain placeholder values
  const isMockEnabled = !ADZUNA_APP_ID || ADZUNA_APP_ID === 'your-adzuna-app-id';

  if (isMockEnabled) {
    console.log("Using Mock Data for Jobs API");
    // Return mock listing items
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          results: mockJobs.filter(job => 
            job.title.toLowerCase().includes(keyword.toLowerCase()) || 
            job.company.display_name.toLowerCase().includes(keyword.toLowerCase())
          ),
          count: mockJobs.length
        });
      }, 800);
    });
  }

  try {
    const response = await axios.get(`${BASE_URL}/${page}`, {
      params: {
        app_id: ADZUNA_APP_ID,
        app_key: ADZUNA_APP_KEY,
        what: keyword,
        where: location,
        results_per_page: 20
      }
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching jobs from Adzuna API:", error);
    throw error;
  }
};

const mockJobs = [
  {
    id: "mock-1",
    title: "Junior React Developer",
    company: { display_name: "TechCorp" },
    location: { display_name: "London, UK" },
    salary_min: 35000,
    salary_max: 45000,
    description: "We are looking for a passionate Junior React Developer with 1+ years experience in HTML, CSS and Javascript to join our growing team. You will be helping us build state of the art web applications with React.",
    created: "2026-03-12",
    latitude: 51.5074,
    longitude: -0.1278
  },
  {
    id: "mock-2",
    title: "UX/UI Designer Intern",
    company: { display_name: "Designly" },
    location: { display_name: "Remote" },
    salary_min: 20000,
    salary_max: 25000,
    description: "Join our design team as an intern and create beautiful layout interfaces for our mobile apps and desktop websites. Must have Figma skills and a strong portfolio.",
    created: "2026-03-14",
    latitude: 53.4808,
    longitude: -2.2426
  },
  {
    id: "mock-3",
    title: "Software Engineer",
    company: { display_name: "DataSync" },
    location: { display_name: "Manchester, UK" },
    salary_min: 40000,
    salary_max: 50000,
    description: "DataSync is seeking a back-end software engineer with Python and SQL experience. You will maintain our core systems and improve database query processing speeds.",
    created: "2026-03-15",
    latitude: 53.4808,
    longitude: -2.2426
  },
  {
    id: "mock-4",
    title: "Product Management Intern",
    company: { display_name: "InnovateHub" },
    location: { display_name: "Birmingham, UK" },
    salary_min: 22000,
    salary_max: 27000,
    description: "Looking for an enthusiastic intern to join our product management team. Learn to design specs, map wireframes, and lead developer scrums and team synchronizations.",
    created: "2026-03-16",
    latitude: 52.4862,
    longitude: -1.8904
  }
];
