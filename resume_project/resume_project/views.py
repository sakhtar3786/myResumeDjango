# resume_project/views.py
from django.shortcuts import render

def resume_view(request):
    resume_data = {
        'name': 'Subhan Akhtar',
        'email': 'sakhtar3786@gmail.com',
        'phone': '+919540335857',
        'address': 'Najafgarh, Delhi, India',
        'summary': 'Upcoming MS in Computer Science student at NYU...',
        'skills': ['Python', 'C++', 'Data Structures', 'Algorithms', 'Operating Systems', 'System Design', 'Data Science'],
        'experience': [
            {
                'title': 'Quantitative Trader',
                'company': 'Da Vinci Derivatives',
                'duration': 'July 2023 – August 2023',
                'responsibilities': [
                    'Completed training on options and pricing models, including Black-Scholes Model.',
                    'Acquired in-depth knowledge of options\' greeks and their implications in financial markets.',
                ],
            },
            {
                'title': 'Summer Internship',
                'company': 'Intel',
                'duration': 'June 2022 – July 2022',
                'responsibilities': [
                    'Worked on Gaudi 2, Intel\'s Deep Learning Accelerator developed by Habana.',
                ],
            },
        ],
        'education': [
            {
                'degree': 'MS in Computer Science',
                'institution': 'New York University',
                'duration': 'Sept 2024 - Upcoming',
                'details': [
                    'Research focus on machine learning and artificial intelligence.',
                ],
            },
            {
                'degree': 'B. Tech in Electrical Engineering',
                'institution': 'Indian Institute of Technology, Delhi',
                'duration': 'May 2023',
                'details': [
                    'JEE Advanced Rank: 444',
                ],
            },
            {
                'degree': 'School',
                'institution': 'C R Oasis Convent School, Najafgarh',
                'duration': '2019',
                'details': [
                    'Kishore Vaigyanik Protsahan Yojana(2017): Secured AIR 276',
                    'Kishore Vaigyanik Protsahan Yojana(2018): Secured AIR 1105',
                ],
            },
            {
                'degree': 'School',
                'institution': 'Gyan Bharati School, Saket',
                'duration': '2017',
                'details': [
                    'Junior Science Talent Search Exam(2015 - 2016): Secured Rank 25 in Delhi among 19674 candidates and got scholarship from Directorate of Education, Govt. of N.C.T. Delhi.',
                ],
            },
        ],
        'projects': [
            {
                'title': 'Analysis of Super-Resolution Techniques(Prof. Manan Suri)',
                'duration': 'April 2023 - June 2023',
                'details': [
                    'Conducted an in-depth study of the historical advancements in super resolution techniques, encompassing Bicubic Interpolation, SRCNN, SRResNet, EDSR , SRGAN, and ESRGAN.',
                    'Utilised various metrics to assess and compare the effectiveness and performance of different super resolution algorithms, like MSE, PSNR and SSIM.',
                ],
            },
            {
                'title': 'Analytics Portal of eTransport(Dr Yogesh Kumar Singh)',
                'duration': 'November 2022 - April 2023',
                'details': [
                    'Worked with analytics team in the development of analytics portal of eTransport at National Informatics Centre Services Incorporated.',
                    'Interacted with the current users of the portal to ask for their requirements and develop the portal according to those requirements.'
                ],
            },
            {
                'title': 'TCGA Data Analysis(Prof. Imtaiyaz Hassan)',
                'duration': 'June 2020 - January 2021',
                'details': [
                    'Worked on TCGA data analysis to discover potential genomic biomarkers of lung cancer.',
                    'The Cancer Genome Atlas is an important genomics programme which molecularly characterises thousands of primary cancers.',
                ],
            },
            {
                'title': 'Image Processing(Prof. Prem Kalra)',
                'duration': 'Oct 2019 - Nov 2019',
                'details': [
                    'Developed an Edge Detection Tool for precise image analysis.',
                ],
            },
            {
                'title': 'Dynamic Memory Allocator(Prof. Rahul Garg)',
                'duration': 'November 2020 - December 2020',
                'details': [
                    'Implemented memory allocation and deallocation mechanisms for computer tasks.',
                ],
            },
            {
                'title': 'Analysis of Indian Economy(Prof. Saurabh Bikas Paul)',
                'duration': 'September 2020 - January 2021',
                'details': [
                    'Estimated Cobb-Douglas equation parameters and predicted Indian Economy growth with Linear Regression.',
                ],
            },
        ],
        'extra_curricular': [
            'Covid Volunteer: Covid Volunteer at Khadim-e-Insaniyat Foundation during the first COVID-19 wave.',
            'Freshers Inter-Hostel: Represented Vindhayachal Hostel in football and achieved 3rd position in basketball.',
            'Support Society Volunteer: Worked with Support Society(2S), an NGO registered with Darpan Portal, to raise awareness and guide marginalised students with regards to higher education and future job prospects in different fields.',
            'Academic Mentor: Assisted first-year students from four hostels with academic preparation and resolving doubts.',
        ],
    }
    return render(request, 'resume.html', {'resume': resume_data})
