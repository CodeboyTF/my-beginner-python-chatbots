

import tkinter as tk
from nltk.chat.util import Chat, reflections

Possible_career_outcomes = [
    ["Hi|Hello|Hey", ["Hi Learner","Hello Scholar","Hey User","How Are You?","Hi!Welcome!!","Hello Student!"]],
    ["How Are You?",["I Am fine How Are You?","Welcome How may i Help"]],
    ["Can you Help Me?",["Yes !!Ofcause I can Help you","How May I be of Assistance?","I Can Help You With Your Career path"]],

    ["What Course Can i Take to be a Software Developer?",[" Computer Science|Computer Systems|Information Technology|Programming Lessons From The Internet."]],
    ["Where can i study information Technology",["you can study at Vaal University of Techology,Tshwane University of Technology and Cape Penisula,University of Johannesburg,Durban University of Technology or you can go about it via college Learning"]],
    ["What is a SOftware Developer?",["A software developer is a professional who designs, creates, tests, and maintains software applications and systems. Software developers are responsible for the entire software development lifecycle, from conceptualization and design to coding, testing, deployment, and ongoing maintenance."]],
    ["what is the salary of a software developer?",["Salaries for software developers in South Africa can vary based on factors such as experience, location within the country, the specific industry, and the skills of the individual developer. Here is a general salary range for software developers in South Africa: (1.Entry-Level (0-2 years of experience): ZAR 150,000 to ZAR 350,000 per year or more),(2.Mid-Level (3-5 years of experience): ZAR 350,000 to ZAR 650,000 per year or more.),(Senior-Level (5+ years of experience): ZAR 650,000 to ZAR 1,200,000 per year or more.),Software Development Managers and Architects: Salaries for managerial and architectural roles can vary widely but typically range from ZAR 800,000 to ZAR 1,500,000 or more per year.It's important to note that these salary ranges are approximate and can vary based on the location within South Africa (cities like Johannesburg, Cape Town, and Durban may offer higher salaries), the specific company, and the demand for specific skills or technologies. Additionally, benefits and bonuses can also impact overall compensation.To get a more accurate and up-to-date picture of software developer salaries in South Africa, it's recommended to consult local job boards, salary surveys, and speak with professionals working in the field. Salaries may also change over time due to economic conditions and industry trends."]],
    ["what are the requirements to study Information Technology|what are the requirement to do information Technology",[]],

    ["what is mechanical engineering",["Mechanical engineering is a branch of engineering that involves designing, analyzing, manufacturing, and maintaining mechanical systems. It applies principles of physics, mathematics, material science, and engineering to develop a wide range of products and machinery, including heating and cooling systems, engines, aircraft, and more. Mechanical engineers work in various industries and are responsible for tasks such as designing, analyzing, and ensuring the efficient production of mechanical components and systems. They also work with concepts like thermodynamics, fluid mechanics, and materials science to make informed decisions in their designs. Overall, mechanical engineering plays a crucial role in technological advancements and impacts many aspects of our daily lives."]],
    ["where can i study mechanical engineering|where can i study engineering",["South Africa has several universities and institutions where you can study mechanical engineering. Here are some of the notable universities that offer mechanical engineering programs in South Africa:University of Cape Town (UCT) - Offers a Bachelor of Science in Mechanical Engineering and postgraduate programs.(University of Pretoria - Offers undergraduate and postgraduate programs in mechanical engineering.),(University of the Witwatersrand (Wits) - Offers a Bachelor of Science in Mechanical Engineering and various postgraduate options.),(Stellenbosch University - Offers a Bachelor of Engineering in Mechanical Engineering and postgraduate programs.),(University of KwaZulu-Natal - Offers a Bachelor of Science in Mechanical Engineering and postgraduate studies in mechanical engineering.),(University of Johannesburg (UJ) - Offers undergraduate and postgraduate degrees in mechanical engineering through its Faculty of Engineering and the Built Environment.),(Cape Peninsula University of Technology (CPUT) - Offers a National Diploma and a Bachelor of Technology in Mechanical Engineering.),(Nelson Mandela University - Offers a Bachelor of Technology in Mechanical Engineering and various postgraduate programs.),(Durban University of Technology (DUT) - Offers a National Diploma and a Bachelor of Technology in Mechanical Engineering.),(North-West University (NWU) - Offers a Bachelor of Engineering in Mechanical Engineering and postgraduate programs.),(Tshwane University of Technology (TUT) - Offers a National Diploma and a Bachelor of Technology in Mechanical Engineering.),(Central University of Technology (CUT) - Offers a Bachelor of Technology in Mechanical Engineering and postgraduate programs.),(Vaal University of Technology (VUT) - Offers a National Diploma and a Bachelor of Technology in Mechanical Engineering.),Please note that specific program offerings, admission requirements, and curriculum details may vary among these institutions, so it's advisable to visit their respective websites and contact their admissions offices for the most up-to-date information on mechanical engineering programs, application procedures, and admission criteria."]],
    ["what is the salary of a mechanical engineering|how much do Mechanical engineers get paid",["In South Africa, the salary of a mechanical engineer can vary based on factors such as experience, location, industry, and qualifications. On average:Entry-level mechanical engineers in South Africa can expect to earn salaries ranging from approximately ZAR 200,000 to ZAR 350,000 per year.,Mid-level mechanical engineers with a few years of experience may earn between ZAR 350,000 and ZAR 600,000 annually.,Experienced mechanical engineers with significant expertise and years of experience can earn salaries exceeding ZAR 600,000 per year.,These figures are approximate and can vary depending on the specific circumstances and the region within South Africa. Additionally, specialized industries or sectors may offer higher salaries. It's essential to research current salary trends and job listings in your area to obtain the most accurate and up-to-date information on mechanical engineering salaries in South Africa."]],
    ["what are the requirements to study mechanical engineering|what are the requirement to do engineering",["In South Africa, the requirements to study mechanical engineering at the undergraduate level typically include the following:,Educational Requirements:National Senior Certificate (NSC) or equivalent high school diploma.Successful completion of the National Benchmark Test (NBT) or other required assessments (some universities may have specific entrance exams or additional tests).Subject Requirements:Mathematics: You will need to have passed mathematics at a certain level, often at the highest grade available (e.g., Mathematics at NSC level 6 or 7).Physical Science: Some universities may require that you have passed physical science at a specific level.Language Proficiency (If Not a Native English Speaker):If your primary language is not English, you may need to demonstrate your English language proficiency through standardized tests like the Test of English as a Foreign Language (TOEFL) or the International English Language Testing System (IELTS).Application Materials:Completed university application forms.High school transcripts or academic records.Letters of recommendation (if required).Personal statement or essay explaining your interest in mechanical engineering (if required).Minimum Admission Points (APS/NSC Score):South African universities often use an Admission Points Score (APS) or National Senior Certificate (NSC) score to evaluate applicants. Meeting the minimum APS or NSC score for the mechanical engineering program is important.Interviews or Additional Tests (If Required):Some universities may conduct interviews or require additional entrance tests, especially for competitive programs.Health and Safety Requirements:Depending on the university and program, there may be specific health and safety requirements, such as medical examinations or vaccinations, especially for programs with practical components.Portfolio (If Required):In some cases, universities may request a portfolio of your work, especially if the program includes design or creative aspects.It's essential to check the specific admission requirements and criteria for the university you are interested in, as requirements may vary between institutions. Each university in South Africa may have its own set of prerequisites and evaluation methods. Be sure to consult the university's official website or contact their admissions department for the most up-to-date and detailed information on admission requirements for mechanical engineering programs."]],


    ["quit", ["Thank you for using the career advice chatbot. Goodbye!"]],
]



Possible_career_outcomes = Chat(Possible_career_outcomes, reflections)


def send_message():
    user_input = input_entry.get()
    response = Possible_career_outcomes.respond(user_input)
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.insert(tk.END, "Career Bot: " + response + "\n")
    chat_box.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)



root = tk.Tk()
root.title("A.I Career Guide Chatbot")

chat_box = tk.Text(root, state=tk.DISABLED)
input_entry = tk.Entry(root)
# creaet the send button
send_button = tk.Button(root, text="Send", command=send_message)

# the exit button
def exit_app():
    root.destroy()

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

chat_box.pack()
input_entry.pack(fill=tk.BOTH)
chat_box.pack(fill=tk.BOTH, expand=True)
send_button.pack()
exit_button.pack()

root.mainloop()


