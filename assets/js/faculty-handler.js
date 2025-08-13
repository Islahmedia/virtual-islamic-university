// Faculty data object with detailed information
const facultyData = {
    'abu-yahya-noorpuri': {
        name: 'فضیلۃ الشیخ ڈاکٹر حافظ ابو یحییٰ نورپوری',
        title: 'ڈائریکٹر، ورچوئل اسلامک یونیورسٹی',
        qualifications: [
            'پی ایچ ڈی ریسرچ اسکالر، شعبہ اسلامیات، پنجاب یونیورسٹی، لاہور',
            'چیف ایگزیکٹو، اصلاح میڈیا'
        ],
        description: 'تعلیم انسان کی زندگی کا بنیادی حق ہے اور اسلامی تعلیم کے ذریعے ہم نئی نسل کو دین اور دنیا کی بہترین تعلیم فراہم کر سکتے ہیں۔',
        image: 'assets/img/faculty/abu-yahya-noorpuri.jpg'
    },
    'iqbal-khilji': {
        name: 'فضیلۃ الشیخ اقبال خلجی',
        title: 'استاذ علوم اسلامیہ',
        qualifications: [
            'فاضل علوم اسلامیہ + ایم فل',
            'تدریس : 2003 میں علوم اسلامیہ کی تدریس شروع کی، جو کہ تاحال جاری ہے ، وللہ الحمد',
            'مدرس : مرکز انس بن مالک لاہور',
            'وزٹنگ ٹیچنگ فیکلٹی: پنچاب یونیورسٹی لاہور'
        ],
        description: 'فضیلۃ الشیخ اقبال خلجی حفظہ اللہ نے 2003 میں علوم اسلامیہ کی تدریس کا آغاز کیا جو تاحال جاری ہے۔ آپ فاضل علوم اسلامیہ اور ایم فل کی ڈگری رکھتے ہیں۔ مرکز انس بن مالک لاہور میں تدریس کے ساتھ ساتھ پنجاب یونیورسٹی لاہور میں وزٹنگ فیکلٹی کے طور پر خدمات انجام دے رہے ہیں۔',
        image: 'assets/img/faculty/iqbal-khilji.jpg'
    },
    'mehtab-asghar': {
        name: 'فضیلۃ الشیخ مہتاب اصغر',
        title: 'مدرس، قباء اسلامک اکیڈمی',
        qualifications: [
            'قرآن مجید کا حفظ',
            'فاضل: وفاق المدارس السلفیہ',
            'فاضل: مدینہ یونیورسٹی',
            'ایم فل (عربی): سرگودھا یونیورسٹی (زیر تعلیم)'
        ],
        description: 'آپ کا تعلق چک نمبر 19 اے ایم ایل، تحصیل پپلاں، ضلع میانوالی سے ہے۔ 2004 میں مرکز ام القری (میانوالی) میں قرآن مجید حفظ کیا۔ 2007 میں قباء اسلامک اکیڈمی میں درس نظامی کا آغاز کیا۔ 2017 میں مدینہ یونیورسٹی سے کلیۃ الحدیث سے بی ایس مکمل کیا۔ فی الوقت قباء اسلامک اکیڈمی میں تدریس، ورچوئل اسلامک یونیورسٹی میں مدرس، اور سرگودھا یونیورسٹی سے ایم فل (عربی) کر رہے ہیں۔',
        image: 'assets/img/faculty/mehtab-asghar.jpg'
    },
    'abu-bakr-siddiq': {
        name: 'فضیلۃ الشیخ حافظ ابوبکر صدیق',
        title: 'متخصص اصول الفقہ و علوم الحدیث',
        qualifications: [
            'حفظ، تجوید، قراءتِ عشرہ، درسِ نظامی',
            'تخصص فی اصول الفقہ: جامعہ اسلامیہ صادق آباد',
            'تخصص فی الحدیث وعلومہ: جامعہ امام بخاری',
            'ایم فل علومِ اسلامیہ: یونیورسٹی آف لاہور'
        ],
        description: '16 جولائی 1997 کو ضلع اوکاڑہ کے گاؤں چک نمبر 17 ون اے ایل میں پیدائش ہوئی۔ کلیۃ القرآن الکریم والتربیۃ الاسلامیۃ سے حفظ، تجوید، قراءت عشرہ اور درس نظامی مکمل کر کے 2018 میں فراغت۔ تخصص فی اصول الفقہ کے لیے جامعہ اسلامیہ صادق آباد میں فضیلۃ الشیخ حافظ ثناء اللہ الزاہدی حفظہ اللہ سے استفادہ۔ تخصص فی الحدیث وعلومہ کے لیے جامعہ امام بخاری میں علامہ غلام مصطفیٰ ظہیر امن پوری اور ڈاکٹر ابو یحییٰ نورپوری حفظہما اللہ سے تعلیم حاصل کی۔',
        image: 'assets/img/faculty/abu-bakr-siddiq.jpg'
    },
    'ameer-hamza': {
        name: 'فضیلۃ الشیخ امیر حمزہ',
        title: 'استاذ علوم اسلامیہ',
        qualifications: [
            'حفظ + درس نظامی',
            'ایسوسی ایٹ ڈگری پروگرام: یونیورسٹی آف سرگودھا',
            'ایم اے عربی / ایم اے اسلامیات',
            'ایم ایس (زیر تعلیم): انٹرنیشنل اسلامک یونیورسٹی اسلام آباد'
        ],
        description: 'آپ کا تعلق سرگودھا سے ہے اور عمر 25 سال ہے۔ حفظ اور درس نظامی کی تعلیم مکمل کرنے کے بعد جدید تعلیم کی جانب رخ کیا۔ یونیورسٹی آف سرگودھا سے ایسوسی ایٹ ڈگری پروگرام مکمل کیا، ایم اے عربی اور ایم اے اسلامیات کی ڈگریاں حاصل کیں۔ فی الوقت انٹرنیشنل اسلامک یونیورسٹی اسلام آباد سے ایم ایس کی تعلیم جاری ہے۔ روایتی اسلامی تعلیم اور جدید یونیورسٹی تعلیم کا امتزاج آپ کی شخصیت کا خاصہ ہے۔',
        image: 'assets/img/faculty/ameer-hamza.jpg'
    },
    'abdul-manan-siddiq': {
        name: 'فضیلۃ الشیخ عبدالمنان صدیقی',
        title: 'استاذ علوم اسلامیہ',
        qualifications: [
            'بی اے عربی، دارالعلوم کراچی',
            'ماہر تجوید و قراءت',
            'علوم حدیث میں تخصص'
        ],
        description: 'فضیلۃ الشیخ عبدالمنان صدیقی حفظہ اللہ ایک تجربہ کار استاذ ہیں جو دارالعلوم کراچی سے بی اے عربی کی ڈگری رکھتے ہیں۔ آپ تجوید و قراءت کے ماہر ہیں اور علوم حدیث میں خاص مہارت رکھتے ہیں۔',
        image: 'assets/img/faculty/abdul-manan-siddiq.jpg'
    },
    'arsalan-zuberi': {
        name: 'فضیلۃ الشیخ ارسلان زبیری',
        title: 'استاذ علم قراءات',
        qualifications: [
            'علم قراءات، جامعہ اسلامیہ مدینہ منورہ',
            'حفظ قرآن کریم',
            'تجوید میں مہارت'
        ],
        description: 'فضیلۃ الشیخ ارسلان زبیری حفظہ اللہ نے جامعہ اسلامیہ مدینہ منورہ سے علم قراءات میں تعلیم حاصل کی ہے۔ آپ حفظ قرآن کریم کے حامل ہیں اور تجوید میں خاص مہارت رکھتے ہیں۔',
        image: 'assets/img/faculty/arsalan-zuberi.jpg'
    }
};

// Function to handle faculty card click from index.html
function navigateToFaculty(facultyId) {
    // Store the selected faculty ID in localStorage
    localStorage.setItem('selectedFaculty', facultyId);
    // Navigate to faculty.html
    window.location.href = 'faculty.html';
}

// Function to load and display faculty details on faculty.html
function loadFacultyDetails() {
    // Get the selected faculty ID from localStorage or URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const facultyIdFromUrl = urlParams.get('faculty');
    const facultyIdFromStorage = localStorage.getItem('selectedFaculty');
    
    const selectedFacultyId = facultyIdFromUrl || facultyIdFromStorage;
    
    if (!selectedFacultyId || !facultyData[selectedFacultyId]) {
        // If no specific faculty is selected, show all faculty (default behavior)
        return;
    }
    
    const faculty = facultyData[selectedFacultyId];
    
    // Update the page title
    document.title = `${faculty.name} - ورچوئل اسلامک یونیورسٹی`;
    
    // Update the main heading
    const pageTitle = document.querySelector('.page-title h1');
    if (pageTitle) {
        pageTitle.textContent = faculty.name;
    }
    
    const pageSubtitle = document.querySelector('.page-title p');
    if (pageSubtitle) {
        pageSubtitle.textContent = faculty.title;
    }
    
    // Clear existing faculty list and show only the selected faculty
    const courseList = document.querySelector('.course-list');
    if (courseList) {
        courseList.innerHTML = `
            <div class="course-item">
                <h2 class="course-title">${faculty.name}</h2>
                <div class="course-description">
                    <ul style="list-style-type: disc; padding-right: 20px; margin: 0;">
                        ${faculty.qualifications.map(qual => `<li>${qual}</li>`).join('')}
                    </ul>
                </div>
                <div class="course-meta">
                    <div class="meta-item">
                        <p class="teacher-details">${faculty.description}</p>
                    </div>
                </div>
            </div>
            
            <!-- Navigation back to all faculty -->
            <div class="text-center mt-4">
                <a href="faculty.html" class="btn btn-secondary">
                    <i class="bi bi-arrow-right"></i>
                    تمام اساتذہ دیکھیں
                </a>
            </div>
        `;
    }
    
    // Clear the localStorage after use
    localStorage.removeItem('selectedFaculty');
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on faculty.html page
    if (window.location.pathname.includes('faculty.html')) {
        loadFacultyDetails();
    }
});

// Make functions globally accessible
window.navigateToFaculty = navigateToFaculty;
window.loadFacultyDetails = loadFacultyDetails;
