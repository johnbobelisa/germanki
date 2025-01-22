//app/(tabs)/decks.tsx

import React from 'react'; 
import { View, Text, StyleSheet } from 'react-native';
import { CustomSearchBar } from '@/components/SearchBar';

export default function Tab() {
  return (
    <View style={styles.container}>
      <CustomSearchBar placeholder="Search decks..." />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
