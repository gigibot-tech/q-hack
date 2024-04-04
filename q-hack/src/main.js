/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'
import axios from 'axios'


// Composables
import { createApp } from 'vue'

const app = createApp(App)
app.use(axios, {})

registerPlugins(app)

app.mount('#app')
