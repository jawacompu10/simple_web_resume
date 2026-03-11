class AppNavbar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <nav class="bg-blue-800 text-white shadow-md print:hidden">
            <div class="container mx-auto px-4 py-3 flex justify-between items-center">
                <div class="flex items-center space-x-4">
                    <a href="index.html" class="text-xl font-bold flex items-center">
                        <i class="fa-solid fa-file-invoice mr-2"></i>
                        Really Free Resumes
                    </a>
                    <a href="index.html" class="hover:text-blue-200 text-sm hidden sm:block">
                        <i class="fa-solid fa-gauge-high mr-1"></i> Dashboard
                    </a>
                </div>
                
                <div class="flex items-center space-x-4" id="creator-corner">
                    <span class="text-xs font-semibold uppercase tracking-wider text-blue-300 hidden md:block">Creator Corner:</span>
                    <a href="https://www.linkedin.com/in/jawahar-vignesh-36418022/" target="_blank" class="hover:text-blue-200 transition-colors" title="LinkedIn">
                        <i class="fa-brands fa-linkedin text-xl"></i>
                    </a>
                    <a href="https://github.com/jawacompu10/simple_web_resume" target="_blank" class="hover:text-blue-200 transition-colors" title="GitHub Project">
                        <i class="fa-brands fa-github text-xl"></i>
                    </a>
                    <button @click="showContactModal = true" class="bg-yellow-500 hover:bg-yellow-400 text-blue-900 font-bold py-1 px-4 rounded-full transition-all transform hover:scale-105 text-sm">
                        Work With Me
                    </button>
                </div>
            </div>
        </nav>
        `;
    }
}

class ContactModal extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <div x-show="showContactModal" 
             x-cloak
             class="fixed inset-0 z-50 overflow-y-auto" 
             aria-labelledby="modal-title" role="dialog" aria-modal="true">
            <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                <div x-show="showContactModal" 
                     x-transition:enter="ease-out duration-300"
                     x-transition:enter-start="opacity-0"
                     x-transition:enter-end="opacity-100"
                     x-transition:leave="ease-in duration-200"
                     x-transition:leave-start="opacity-100"
                     x-transition:leave-end="opacity-0"
                     @click="showContactModal = false"
                     class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>

                <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                <div x-show="showContactModal"
                     x-transition:enter="ease-out duration-300"
                     x-transition:enter-start="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                     x-transition:enter-end="opacity-100 translate-y-0 sm:scale-100"
                     x-transition:leave="ease-in duration-200"
                     x-transition:leave-start="opacity-100 translate-y-0 sm:scale-100"
                     x-transition:leave-end="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                     class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    
                    <form action="https://formspree.io/f/xgonklyn" method="POST">
                        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                            <div class="sm:flex sm:items-start">
                                <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                                    <i class="fa-solid fa-envelope text-blue-600"></i>
                                </div>
                                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                                    <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                                        Get in touch
                                    </h3>
                                    <div class="mt-4 space-y-4">
                                        <div>
                                            <label for="contact-name" class="block text-sm font-medium text-gray-700">Name</label>
                                            <input type="text" name="name" id="contact-name" required class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                                        </div>
                                        <div>
                                            <label for="contact-email" class="block text-sm font-medium text-gray-700">Email</label>
                                            <input type="email" name="email" id="contact-email" required class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                                        </div>
                                        <div>
                                            <label for="contact-message" class="block text-sm font-medium text-gray-700">Message</label>
                                            <textarea id="contact-message" name="message" rows="4" required class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"></textarea>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                            <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
                                Send Message
                            </button>
                            <button type="button" @click="showContactModal = false" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                                Cancel
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        `;
    }
}

class StorageInfoModal extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <div x-show="showInfoModal" 
             x-cloak
             class="fixed inset-0 z-50 overflow-y-auto" 
             aria-labelledby="modal-title" role="dialog" aria-modal="true">
            <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                <div x-show="showInfoModal" 
                     x-transition:enter="ease-out duration-300"
                     x-transition:enter-start="opacity-0"
                     x-transition:enter-end="opacity-100"
                     x-transition:leave="ease-in duration-200"
                     x-transition:leave-start="opacity-100"
                     x-transition:leave-end="opacity-0"
                     @click="closeModal()"
                     class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>

                <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                
                <div x-show="showInfoModal"
                     x-transition:enter="ease-out duration-300"
                     x-transition:enter-start="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                     x-transition:enter-end="opacity-100 translate-y-0 sm:scale-100"
                     x-transition:leave="ease-in duration-200"
                     x-transition:leave-start="opacity-100 translate-y-0 sm:scale-100"
                     x-transition:leave-end="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                     class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div class="sm:flex sm:items-start">
                            <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                                <i class="fa-solid fa-database text-blue-600"></i>
                            </div>
                            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                <h3 class="text-lg leading-6 font-bold text-gray-900 mb-4" id="modal-title">
                                    About Local Storage
                                </h3>
                                <div class="space-y-4">
                                    <div>
                                        <h4 class="font-bold text-green-700 flex items-center">
                                            <i class="fa-solid fa-circle-check mr-2"></i> Pros
                                        </h4>
                                        <ul class="list-disc ml-6 text-sm text-gray-600 mt-1">
                                            <li><strong>Privacy:</strong> Your data stays with you. It is never uploaded to any server.</li>
                                            <li><strong>Speed:</strong> Instant loading and saving since everything happens on your machine.</li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h4 class="font-bold text-red-700 flex items-center">
                                            <i class="fa-solid fa-circle-exclamation mr-2"></i> Cons
                                        </h4>
                                        <ul class="list-disc ml-6 text-sm text-gray-600 mt-1">
                                            <li><strong>Persistence:</strong> If you clear browser data or browse in incognito mode, you lose your data unless you have downloaded it already.</li>
                                            <li><strong>Device Bound:</strong> Your profiles are only available on the specific browser and device where you created them.</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                        <button type="button" @click="closeModal()" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:w-auto sm:text-sm">
                            Got it!
                        </button>
                    </div>
                </div>
            </div>
        </div>
        `;
    }
}

customElements.define('app-navbar', AppNavbar);
customElements.define('contact-modal', ContactModal);
customElements.define('storage-info-modal', StorageInfoModal);
