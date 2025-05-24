<template>
  <div ref="captureArea" class="card overflow-x-auto">
    <button id="save-to-img-btn" @click="capture">Save Visual</button>
    <OrganizationChart
      v-model:selectionKeys="selection"
      :value="ChartData"
      collapsible
      selectionMode="single"
    >
      <template #default="slotProps">
        <div class="card">
          <div class="header">
            {{ slotProps.node.label }}
          </div>
          <div class="value">
            {{ slotProps.node.value }}
          </div>
          <hr />
          <div class="comparative-value">
            {{ slotProps.node.comparator }}
          </div>
        </div>
      </template>
    </OrganizationChart>
  </div>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue'
import html2canvas from 'html2canvas'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from '../streamlit'

interface ParsedArgs {
  data: TreeNode
}

interface TreeNode {
  key: string
  label: string
  value: string
  comparator: string
  styleClass: string
  children?: TreeNode[]
}

export default defineComponent({
  props: {
    args: {
      type: Object as PropType<ParsedArgs>,
      required: true,
    },
  },
  data() {
    return {
      ChartData: {} as TreeNode,
      selection: {},
      screenShot:'',
    }
  },
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize
  },
  mounted() {
    this.ChartData = this.$props.args.data
  },
  watch: {
    selection(NewVal) {
      const SelectedValue = Object.keys(NewVal)[0]
      if (SelectedValue) {
        Streamlit.setComponentValue(SelectedValue)
      }
    },
  },
  methods: {
    capture() {
      const el = this.$refs.captureArea as HTMLElement
      if (el === null){
        return
      }
      const orgChartElement = document.querySelector('.p-organizationchart-table') as HTMLElement
      if (orgChartElement === null){
        return
      }
      const widthx = orgChartElement.offsetWidth +50
      html2canvas(el,{scale:3,width:widthx,backgroundColor:'#EDEADE'}).then(canvas => {
        this.screenShot = canvas.toDataURL("image/png");
        const link = document.createElement('a');
        link.download = 'screenshot.png';
        link.href = this.screenShot;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }).catch(error => {
        console.error("Capture failed:", error);
      })
    }
  },
})
</script>
