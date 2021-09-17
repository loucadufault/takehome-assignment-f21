<template>
  <div>
    <p>I'm a Counter!</p>
    <p>Current count is: {{count}}</p>
    <span>
      <button v-on:click="count++">Increment</button>
      <button v-on:click="count--">Decrement</button>
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  }
};
</script>

<style>
</style>

