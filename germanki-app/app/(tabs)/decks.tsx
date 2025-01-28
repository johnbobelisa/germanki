// app/(tabs)/decks.tsx

import React from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';
import RNESearchBar from '@/components/SearchBar';

import { FlashList } from "@shopify/flash-list";
import { SafeAreaView } from 'react-native-safe-area-context';
import { FAB } from '@rneui/themed'; // Import FAB from @rneui/themed
import { useNavigation } from '@react-navigation/native'; // If using React Navigation

const data = Array.from({ length: 100 }, (_, i) => `Item ${i + 1}`);

export default function Tab() {
  const navigation = useNavigation(); // Initialize navigation if needed

  const handleAddPress = () => {
    // Define what happens when the FAB is pressed
    // For example, navigate to an "Add Deck" screen
    // navigation.navigate('AddDeck');
    console.log('FAB Pressed');
  };

  return (
    <SafeAreaView style={styles.container}>
      <RNESearchBar />

      <FlashList
        data={data}
        renderItem={({ item }) => (
          <View style={styles.itemContainer}>
            <Text style={styles.itemText}>{item}</Text>
          </View>
        )}
        estimatedItemSize={100}
        contentContainerStyle={styles.listContent}
      />

      {/* Floating Action Button */}
      <FAB
        icon={{ name: 'plus', type: 'font-awesome', color: '#fff' }} // Plus icon
        color="#007AFF" // Customize the FAB color
        size="large" // Set the size to large
        onPress={handleAddPress} // Handle press event
        placement="right" // Use 'right' as placeholder; we'll override placement with style
        style={styles.fab} // Custom styles for positioning
        visible={true} // Ensure the FAB is visible
        upperCase={false} // Optional: Keep icon as is
      />
    </SafeAreaView>
  );
}

const { width, height } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    position: 'relative', // Ensure relative positioning for absolute children
  },
  listContent: {
    paddingHorizontal: 16,
    paddingBottom: 100, // Add padding to prevent content from being hidden behind the FAB and tab bar
  },
  itemContainer: {
    width: '100%',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  itemText: {
    fontSize: 16,
    textAlign: 'left',
    width: '100%',
  },
  fab: {
    position: 'absolute',
    bottom: 30, // Adjust based on the height of your tab bar
    alignSelf: 'center', // Center horizontally
    // Optional: Add shadow for better visibility
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3.84,
    elevation: 5, // For Android shadow
  },
});
