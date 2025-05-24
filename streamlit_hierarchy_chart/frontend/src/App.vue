<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <OrgChart :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import OrgChart from './components/OrgChart.vue'

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).

import WithStreamlitConnection from './streamlit/WithStreamlitConnection.vue'

export default defineComponent({
  name: 'App',
  components: {
    OrgChart,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0px;
}
</style>
