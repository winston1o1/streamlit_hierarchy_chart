import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import OrganizationChart from 'primevue/organizationchart'

const app = createApp(App)
app.use(PrimeVue,
  {
  theme: {
    preset: Aura,
    options: {
      prefix: 'p',
      darkModeSelector: 'system',
      cssLayer: false,
    },
  },
}
)

app.component('OrganizationChart', OrganizationChart)

app.mount('#app')
